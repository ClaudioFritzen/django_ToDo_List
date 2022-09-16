from http import client
from django.test import Client


def test_home_status_code(cliente:Client):
    reposta = client.get('/')
    assert reposta.status_code == 200 