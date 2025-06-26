import os

import requests
##from marshmallow import ValidationError

def fetch_api_petstore(pet_id):
    url = f"https://petstore.swagger.io/v2/pet/{pet_id}"
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    return response.json()
