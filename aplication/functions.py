import json

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def fetchBravas():
    url = "https://192.168.10.4:8090/portaria/v1/bravas/config/user/"

    payload = json.dumps({
        "config": {
            "action": "getUserList",
            "mode": 0,
            "start": 0,
            "size": 999999
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)

    return response
