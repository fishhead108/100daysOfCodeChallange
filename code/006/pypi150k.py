import requests
import xmlrpc.client as xmlrpclib
from dateutil import parser
from multiprocessing.dummy import Pool as ThreadPool

NUM_PACKS_TO_REACH = 150000
PYPI = 'https://pypi.python.org/pypi'

client = xmlrpclib.ServerProxy(PYPI)
packages = client.list_packages()

packages_time = {}

def fetch_date(package_name):
    url = f'{PYPI}/{package_name}/json'
    r = requests.get(url)
    # СПИСОК УСПЕШНЫХ КОДОВ !!!
    #if r.status_code == requests.codes.ok:
    if r.status_code == 200:
        if len(r.json()['urls']) > 0:
            time = parser.parse(r.json()['urls'][-1]['upload_time'])
            packages_time[time] = package_name
        else:
            packages_time[None] = package_name
    else:
        pass

pool = ThreadPool(10)
pool.map(fetch_date, packages)
pool.close()
pool.join()


if __name__ == "__main__":
    pass