from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_dev_retornar_ola_mundo():
    client = TestClient(app)
    response = client.get('/')
    assert response.json() == {'message': 'Olá Mundo!!'}
    assert response.status_code == HTTPStatus.OK
