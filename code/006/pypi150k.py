# https://www.digitalocean.com/community/tutorials/a-guide-to-time-series-forecasting-with-arima-in-python-3
# https://www.analyticsvidhya.com/blog/2016/02/time-series-forecasting-codes-python/
# https://www.digitalocean.com/community/tutorials/a-guide-to-time-series-forecasting-with-prophet-in-python-3
# http://machinelearningmastery.com/time-series-forecasting-python-mini-course/

import pickle
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
    # if r.status_code == requests.codes.ok:
    if r.status_code == 200:
        if len(r.json()['urls']) > 0:
            time = r.json()['urls'][-1]['upload_time']
            packages_time[package_name] = time
            packages.remove(package_name)
        else:
            packages_time[package_name] = None
            packages.remove(package_name)
    else:
        pass


pool = ThreadPool(10)
pool.map(fetch_date, packages)
pool.close()
pool.join()

pickle.dump(packages_time, open("normalTime.p", "wb"))

pack = pickle.load(open("normalTime.p", "rb"))
dct = sorted(pack.items(), key=lambda p: p[1], reverse=True)


if __name__ == "__main__":
    pass
