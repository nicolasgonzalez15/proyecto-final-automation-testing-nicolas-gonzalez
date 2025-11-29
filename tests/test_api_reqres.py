import requests
import pytest
import json
from utils.logger import logger

# Obtener usuario
def test_get_user(url_base,header_request):
    logger.info(f"Realizando solicitud GET a {url_base}")
    # URL Base
    #url = f"{url_base}/?page=2"
    url = f"{url_base}/2"

    # Obtenemos Response
    response = requests.get(url,headers=header_request)

    logger.info(f"Status code: {response.status_code}")
    # VALIDACIÓN RESPUESTA CORRECTA
    assert response.status_code == 200

    # Cuerpo de la respuesta
    data = response.json()
    data_formatted = json.dumps(data,indent=4)
    print(f"Data con formato:{data_formatted}")

    assert data['data']['id'] == 2
    

# Obtener usuario
def test_create_user(url_base,header_request):
    payload = {
        "name": "José",
        "job": "Profesor"
    }

    response = requests.post(url_base,headers=header_request,json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data['name'] == payload['name']


# Obtener usuario
def test_delete_user(url_base,header_request):

    response = requests.delete(f"{url_base}/2",headers=header_request)

    assert response.status_code == 204

