# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/00_core.ipynb (unless otherwise specified).

__all__ = ['is_container', 'flatten_recursive', 'flatten_list_of_lists', 'deduplicate_list', 'chunk_list',
           'filter_passing', 'set_global_pool', 'close_global_pool', 'refresh_global_pool', 'new_pool_parallel',
           'maybe_parallel', 'GLOBAL_POOL', 'download_files']

# Cell
from .imports import *
from multiprocessing import get_context
import requests
import zipfile

# Cell
def is_container(x):
    "check if `x` is a container (used for parallel processing)"
    if isinstance(x, (list, tuple, np.ndarray)):
        return True
    else:
        return False

def flatten_recursive(list_of_lists):
    "Recursively flattel list of lists"
    flat_list = []
    for item in list_of_lists:
        if type(item) == list:
            flat_list += flatten_recursive(item)
        else:
            flat_list.append(item)

    return flat_list

def flatten_list_of_lists(list_of_lists):
    "Flattens list of lists (not recursive)"
    return [item for sublist in list_of_lists for item in sublist]

def deduplicate_list(l):
    "Deduplicates list l"
    return list(set(l))

def chunk_list(input_list, chunksize):
    'Breaks `input_list` into chunks of size `chunksize`, ragged on last list'
    return [input_list[i:i+chunksize] for i in range(0, len(input_list), chunksize)]

def filter_passing(inputs, bools):
    'Subsets `inputs` (list) by `bools` (list of bools)'
    assert len(inputs)==len(bools), '`inputs` and `bools` must have the same length'
    return [inputs[i] for i in range(len(inputs)) if bools[i]]

# Cell

GLOBAL_POOL = None
os.environ['max_global_threads'] = '2000'

def set_global_pool(cpus=None):
    global GLOBAL_POOL
    if GLOBAL_POOL is not None:
        close_global_pool()

    if cpus is None:
        GLOBAL_POOL = None
    else:
        GLOBAL_POOL = Pool(processes=cpus)
        GLOBAL_POOL.uses = 0

def close_global_pool():
    global GLOBAL_POOL
    if GLOBAL_POOL is not None:
        GLOBAL_POOL.close()
        del GLOBAL_POOL
        GLOBAL_POOL = None
        gc.collect()

def refresh_global_pool():
    global GLOBAL_POOL
    if GLOBAL_POOL is not None:
        cpus = GLOBAL_POOL._processes
        close_global_pool()
        set_global_pool(cpus=cpus)

def new_pool_parallel(func, iterable, cpus=None, **kwargs):
    p_func = partial(func, **kwargs)
    if is_container(iterable):

        if cpus is None:
            if 'ncpus' in os.environ.keys():
                cpus = int(os.environ['ncpus'])
            else:
                cpus = 0

        processes = min(cpus, len(iterable))

        if processes == 1:
            # spinning up a single pool has more overhead
            processes = 0

        if processes == 0:
            output = [p_func(i) for i in iterable]

        else:
            with Pool(processes=cpus) as p:
                output = p.map(p_func, iterable)

    else:
        output = p_func(iterable)

    return output

def maybe_parallel(func, iterable, cpus=None, **kwargs):
    global GLOBAL_POOL

    p_func = partial(func, **kwargs)

    if is_container(iterable):
        if cpus is not None:

            output = new_pool_parallel(func, iterable, cpus, **kwargs)

        elif GLOBAL_POOL is not None:
            output = GLOBAL_POOL.map(p_func, iterable)
            GLOBAL_POOL.uses += 1
            if GLOBAL_POOL.uses > int(os.environ['max_global_threads']):
                refresh_global_pool()
                gc.collect()

        else:
            output = [p_func(i) for i in iterable]

    else:
        output = p_func(iterable)

    return output


# Cell

def download_files():
    if not os.path.exists('files'):
        r = requests.get('https://dmai-mrl.s3.us-west-2.amazonaws.com/mrl_public/files.zip')

        with open('files.zip', 'wb') as f:
            f.write(r.content)

        with zipfile.ZipFile('files.zip', 'r') as zip_ref:
            zip_ref.extractall('.')

        os.remove('files.zip')