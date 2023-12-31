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
            "size": 99999
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)

    return response


def insertBravas(ip, nome, matricula, tag, seg=False, ter=False, qua=False, qui=False, sex=False, sab=False, dom=False,
                 cafe_manha=False, almoco=False,
                 cafe_pendura=False,
                 cafe_tarde=False, janta=False):
    grupos = ['KIT']

    if seg:
        grupos.append("seg")
    if ter:
        grupos.append("ter")
    if qua:
        grupos.append("qua")
    if qui:
        grupos.append("qui")
    if sex:
        grupos.append("sex")
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

    grupos = []

    if response.status_code == 200:
        data = response.json()
        if 'config' in data and 'name' in data['config'] and 'groups' in data['config']:
            nome = data['config']['name']
            grupos.extend(data['config']['groups'])

    if estado and "KIT" not in grupos:
        grupos.append("KIT")

    if not estado and "KIT" in grupos:
        grupos.remove("KIT")

    payload = {
        "config": {
            "action": "editUser",
            "target": {
                "name": nome
            },
            "groups": grupos,
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


def delbravas(ip, name):
    url = f'https://{ip}:8090/portaria/v1/bravas/config/user/'

    payload = {
        "config": {
            "action": "deleteUser",
            "target": {
                "name": f"{name}"
            },
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


def seluser(ip, name):
    url = f'https://{ip}:8090/portaria/v1/bravas/config/user/'

    payload = {
        "config": {
            "action": "getUser",
            "target": {
                "name": f"{name}"
            }
        }
    }

    headers = {
        'Content-type': 'application/vnd.api+json',
        'Accept': 'application/vnd.api+json'
    }

    response = requests.post(url, json=payload, headers=headers, verify=False)
    #print the entire json
    print(response.json())
    return response


def editbravas(ip, nome, tag, ativado, seg=True, ter=True, qua=True, qui=True, sex=True, sab=True, dom=True,
               cafe_manha=False, almoco=False,
               cafe_pendura=False,
               cafe_tarde=False, janta=False):
    grupos = []

    if seg:
        grupos.append("seg")
    if ter:
        grupos.append("ter")
    if qua:
        grupos.append("qua")
    if qui:
        grupos.append("qui")
    if sex:
        grupos.append("sex")
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
            "action": "editUser",
            "target": {
                "name": f"{nome}"
            },
            "enabled": f"{ativado}",
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


def cadMassa(ip, nome, matricula, tag, ativado, cafe_manha, almoco, cafe_pendura,
             cafe_tarde, janta):
    grupos = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]

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
            "enabled": f"{ativado}",
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


def delMassa(ip, name, matricula):
    url = f'https://{ip}:8090/portaria/v1/bravas/config/user/'

    payload = {
        "config": {
            "action": "deleteUser",
            "target": {
                "name": f"{name} - {matricula}"
            },
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
