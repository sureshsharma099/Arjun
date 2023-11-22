import re
import json
import time
import random
import warnings
import requests

import core.config

from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

warnings.filterwarnings('ignore') # Disable SSL related warnings

def requester(url, data, headers, GET, delay):
    if core.config.globalVariables['jsonData']:
        data = json.dumps(data)
    if core.config.globalVariables['stable']:
        delay = random.choice(range(6, 12))
    time.sleep(delay)
    headers['Host'] = re.search(r'https?://([^/]+)', url).group(1)
    if GET:
        response = requests.get(url, params=data, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}, verify=False, allow_redirects=False, timeout=10)
    elif core.config.globalVariables['jsonData']:
        response = requests.post(url, json=data, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}, verify=False, allow_redirects=False, timeout=10)
    else:
        response = requests.post(url, data=data, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}, verify=False, allow_redirects=False, timeout=10)
    return response
