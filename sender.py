from typing import Dict
from constant import ASTUTIA_URL
import requests

def send_to_astutia(endpoint: str=None, data: Dict={}, headers: Dict={}, request_type=1):
    if request_type == 1:
        url = ASTUTIA_URL + endpoint
        resp = requests.get(url=url, params=data, headers=headers)
        return {
            'status_code': resp.status_code,
            'data': resp.json()
        }
    if request_type == 2:
        url = ASTUTIA_URL + endpoint
        resp = requests.post(url=url, data=data, headers=headers)
        return {
            'status_code': resp.status_code,
            'data': resp.json()
        }
    return {
        'status_code': None,
        'data': None
    }
