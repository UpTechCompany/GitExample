import pytest
from flask import Response
from main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_report_existing_key_and_format(client):
    # Проверяем запрос существующего ключа и формата
    response = client.get("/api/report/units/csv")
    assert response.status_code == 200
    assert response.mimetype == "application/csv"
    assert response.data == f"units"  # Проверяем, что в ответе верный ключ

def test_get_report_nonexistent_key(client):
    # Проверяем запрос несуществующего ключа
    response = client.get("/api/report/nonexistent_key/csv")
    assert response.status_code == 500
    assert f"Такого ключа не существует" in response.data

def test_get_report_unavailable_format(client):
    # Проверяем запрос существующего ключа, но недоступного формата
    response = client.get("/api/report/units/pdf")
    assert response.status_code == 500
    assert f"Ключ существует, но этот формат экспорта недоступен" in response.data
