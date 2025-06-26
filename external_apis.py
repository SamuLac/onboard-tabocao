import os

import requests
##from marshmallow import ValidationError

def fetch_api_petstore():
    response = requests.get("https://petstore.swagger.io/v2/pet/1", timeout=15)
    response.raise_for_status()
    return response.json()
