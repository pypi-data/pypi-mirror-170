#!/usr/bin/env python3

import argparse
import staremaster.products
import glob
import multiprocessing
import itertools
import filelock
import pkgutil
import importlib
import re


def create_grid_sidecar(grid, out_path, n_workers):
    grid = grid.lower()
    if grid == 'imerg':
        granule = staremaster.products.IMERG()
    elif grid[0] == 'h' and grid[3] == 'v':
        granule = staremaster.products.ModisTile(grid)
    else:
        print('unknown grid')
        exit()
    granule.create_sidecar(out_path, n_workers=n_workers)


def create_sidecar(file_path, n_workers, product, cover_res, out_path, archive):
    print(f'creating sidecar for {file_path}')
    if product is None:
        product = guess_product(file_path)

    product = product.upper()

    if product == 'MOD05':
        granule = staremaster.products.MOD05(file_path)
    elif product == 'MOD09':
        granule = staremaster.products.MOD09(file_path)
    elif product == 'VNP02DNB':
        granule = staremaster.products.VNP02DNB(file_path)
    elif product == 'VNP03':
        granule = staremaster.products.VNP03(file_path)
    elif product == 'VJ102DNB':
        granule = staremaster.products.VJ102DNB(file_path)
    elif product == 'VJ103DNB':
        granule = staremaster.products.VJ103DNB(file_path)
    elif product == 'CLDMSK_L2_VIIRS':
        granule = staremaster.products.CLMDKS_L2_VIIRS(file_path)
    elif product == 'SSMIS':
        granule = staremaster.products.SSMIS(file_path)
    elif product == 'ATMS':
        granule = staremaster.products.ATMS(file_path)
    else:
        print('product not supported')
        print('supported products are {}'.format(get_installed_products()))
        quit()
    granule.load()
    sidecar = granule.create_sidecar(n_workers=n_workers, cover_res=cover_res, out_path=out_path)

    if archive:
        with filelock.FileLock(archive + '.lock.'):
            with open(archive, 'a') as cat:
                line = '{}, {} \n'.format(file_path, sidecar.file_path)
                cat.writelines(line)


def list_granules(folder, product):
    if not product:
        product = ''

    files = glob.glob(folder + '/*')
    pattern = '.*{product}.*[^_stare]\.(nc|hdf|HDF5)'.format(product=product.upper())
    granules = list(filter(re.compile(pattern).match, files))
    return granules


def guess_product(file_path):
    file_name = file_path.split('/')[-1]
    if 'MOD05_L2' in file_path and '.hdf' in file_name:
        product = 'MOD05'
    elif 'MOD09' in file_path and '.hdf' in file_name:
        product = 'MOD09'
    elif ('VNP03' in file_path or 'VJ103' in file_path) and '.nc' in file_name:
        product = 'VNP03'
    elif ('VNP02DNB' in file_path or 'VJ102DNB' in file_path) and '.nc' in file_name:
        product = 'VNP02DNB'
    elif 'CLDMSK_L2_VIIRS' in file_path and '.nc' in file_name:
        product = 'CLDMSK_L2_VIIRS'
    elif 'SSMIS' in file_path and '.HDF5' in file_name:
        product = 'SSMIS'
    elif 'ATMS' in file_path and '.HDF5' in file_name:
        product = 'ATMS'
    else:
        product = None
        print('could not determine product for {}'.format(file_path))
        quit()
    return product


def remove_archived(file_paths, archive):
    if glob.glob(archive):
        with open(archive, 'r') as cat:
            csv = cat.readlines()
        archived = []
        for row in csv:
            archived.append(row.split(',')[0])
        n_archived = len(archived)
        n_filepaths = len(file_paths)
        print(f'{n_archived} out of {n_filepaths} been recorded in the archive and will not be processed')
        unprocessed = list(set(file_paths) - set(archived))
    else:
        unprocessed = file_paths
    return unprocessed


def get_installed_products():
    starmeaster_path = importlib.util.find_spec('staremaster.products').submodule_search_locations[0]
    products = [name for _, name, _ in pkgutil.iter_modules([starmeaster_path])]
    return products


def main():
    installed_products = get_installed_products()
    parser = argparse.ArgumentParser(description='Creates Sidecar Files')
    parser.add_argument('--folder', metavar='folder', type=str,
                        help='the folder to create sidecars for')
    parser.add_argument('--files', metavar='files', nargs='+', type=str,
                        help='the files to create a sidecar for')
    parser.add_argument('--grid', metavar='files', type=str,
                        help='the grid to create a sidecar for (e.g. IMERG, h08v05)')
    parser.add_argument('--out_path', type=str,
                        help='the folder to create sidecars in; default: next to granule')
    parser.add_argument('--product', metavar='product', type=str,
                        help='product (e.g. cldmsk_l2_viirs, hdfeos, l2_viirs, mod05, mod09, vj102dnb, '
                             'vj103dnb, vnp02dnb, vnp03, ssmi)',
                        choices=installed_products, default=None)
    parser.add_argument('--cover_res', metavar='cover_res', type=int,
                        help='max STARE resolution of the cover. Default: min resolution of iFOVs')
    parser.add_argument('--workers', metavar='n_workers', type=int,
                        help='use n_workers (local) dask workers', default=1)
    parser.add_argument('--archive', metavar='archive', type=str,
                        help='''Create sidecars only for granules not listed in the archive file. 
                            Record all create sidecars and their corresponding granules in it.''')
    parser.add_argument('--parallel_files', dest='parallel_files', action='store_true',
                        help='Process files in parallel rather than looking up SIDs in parallel')

    parser.set_defaults(archive=False)
    parser.set_defaults(parallel_files=False)

    args = parser.parse_args()

    if args.files:
        file_paths = args.files
    elif args.folder:
        file_paths = list_granules(args.folder, product=args.product)
    elif args.grid:
        create_grid_sidecar(args.grid, args.out_path, n_workers=args.workers)
        quit()
    else:
        print('Wrong usage; need to specify a folder, file, or grid\n')
        print(parser.print_help())
        quit()

    if args.archive:
        file_paths = remove_archived(file_paths, args.archive)

    if args.parallel_files:
        map_args = zip(file_paths,
                       itertools.repeat(1),
                       itertools.repeat(args.product),
                       itertools.repeat(args.cover_res),
                       itertools.repeat(args.out_path),
                       itertools.repeat(args.archive))
        with multiprocessing.Pool(processes=args.workers) as pool:
            pool.starmap(create_sidecar, map_args)
    else:
        for file_path in file_paths:
            create_sidecar(file_path=file_path,
                           n_workers=args.workers,
                           product=args.product,
                           out_path=args.out_path,
                           cover_res=args.cover_res,
                           archive=args.archive)


if __name__ == '__main__':
    main()
