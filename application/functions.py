import json

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def fetchbravas(ip):
    url = f"https://{ip}:8090/portaria/v1/bravas/config/user/"

    payload = json.dumps({
        "config": {
            "action": "getUserList",
            "mode": 0,
            "start": 0,
            "size": 50
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)

    return response


def insertbravas(ip, nome, matricula, tag, seg_sex=False, sab=False, dom=False, cafe_manha=False, almoco=False,
                 cafe_pendura=False,
                 cafe_tarde=False, janta=False):
    grupos = ['KIT']

    if seg_sex:
        grupos.append("geral")
    if sab:
        grupos.append("sab")
    if dom:
        grupos.append("dom")
    if cafe_manha:
        grupos.append("cafe-manha")
    if almoco:
        grupos.append("almoco")
    if cafe_pendura:
        grupos.append("cafe-pendura")
    if cafe_tarde:
        grupos.append("cafe-tarde")
    if janta:
        grupos.append("jantar")

    url = f'https://{ip}:8090/portaria/v1/bravas/config/user/'
    payload = {
        "config": {
            "action": "addUser",
            "name": f"{nome} - {matricula}",
            "enabled": "True",
            "groups": grupos,
            "tags": [
                f"{tag}"
            ],
            "readers": [
                "ALL"
            ]
        }
    }
    headers = {
        'Content-type': 'application/vnd.api+json',
        'Accept': 'application/vnd.api+json'
    }
    response = requests.post(url, json=payload, headers=headers, verify=False)
    return response


def editkit(ip, nome, estado):
    url = f'https://{ip}:8090/portaria/v1/bravas/config/user/'

    payload = {
        "config": {
            "action": "getUser",
            "target": {
                "name": f"{nome}"
            }
        }
    }

    headers = {
        'Content-type': 'application/vnd.api+json',
        'Accept': 'application/vnd.api+json'
    }

    response = requests.post(url, json=payload, headers=headers, verify=False)



    if estado is True:
        kit = 'KIT'
    else:
        kit = ''

    payload = {
        "config": {
            "action": "editUser",
            "target": {
                "name": f"{nome}"
            },
            "groups": [
                f"{kit}",
            ],
            "readers": [
                "ALL"
            ]
        }
    }

    headers = {
        'Content-type': 'application/vnd.api+json',
        'Accept': 'application/vnd.api+json'
    }

    response = requests.post(url, json=payload, headers=headers, verify=False)
