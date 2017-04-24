NUM_PACKS_TO_REACH = 150000
PYPI = 'https://pypi.python.org/pypi'
import requests
from multiprocessing.dummy import Pool as ThreadPool

try:
     import xmlrpclib
except ImportError:
     import xmlrpc.client as xmlrpclib

client = xmlrpclib.ServerProxy(PYPI)
packages = client.list_packages()

ptime = {}

def fetch_date(package_name):
    url = f'{PYPI}/{package_name}/json'
    r = requests.get(url)
    # СПИСОК УСПЕШНЫХ КОДОВ !!!
    #if r.status_code == requests.codes.ok:
    if r.status_code == 200:
        if len(r.json()['urls']) > 0:
            ptime[r.json()['urls'][-1]['upload_time']] = package_name
        else:
            ptime[None] = package_name
    else:
        pass

pool = ThreadPool(100)
pool.map(fetch_date, packages)


if __name__ == "__main__":
    pass