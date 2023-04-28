import pytest
from app import Flask_App

@pytest.fixture
def client():
    with Flask_App.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Calculator' in response.data

def test_operation_result(client):
    response = client.post('/operation_result/', data=dict(
        Input1='10',
        Input2='5',
        operation='+'
    ))
    assert response.status_code == 200
    assert b'15.0' in response.data

# def test_operation_broken_result(client):
#     response = client.post('/operation_result/', data=dict(
#         Input1='10',
#         Input2='5',
#         operation='-'
#     ))
#     assert response.status_code == 200
#     assert b'15.0' in response.data


def test_operation_result_bad_input(client):
    response = client.post('/operation_result/', data=dict(
        Input1='10',
        Input2='0',
        operation='/'
    ))
    assert response.status_code == 200
    assert b'Bad Input' in response.data
    assert b'You cannot divide by zero' in response.data

def test_operation_result_invalid_input(client):
    response = client.post('/operation_result/', data=dict(
        Input1='10',
        Input2='abc',
        operation='+'
    ))
    assert response.status_code == 200
    assert b'Bad Input' in response.data
    assert b'Cannot perform numeric operations with provided input' in response.data
