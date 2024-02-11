import ssl
context = ssl._create_unverified_context()

import json
import requests
def download_file():
    url = "https://data.gharchive.org/2015-01-01-15.json.gz"
    print (url)
    # res = requests.get(f"https://data.gharchive.org/{file}", verify=False)
    res = requests.get(url, params=PARAMS, verify=False)
    return res
 
res = download_file()


# print (res.status_code)