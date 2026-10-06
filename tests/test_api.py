import pytest
from fastapi.testclient import TestClient
from proyecto_final_orders.main import app

client = TestClient(app)

def test_flujo_creacion_orden():
    # 1. Login y extracción del token JWT
    resp_login = client.post("/login", data={"username": "admin", "password": "secreto"})
    assert resp_login.status_code == 200
    token = resp_login.json()["access_token"]

    # 2. Petición autenticada con el DTO esperado
    headers = {"Authorization": f"Bearer {token}"}
    payload = [
        {"product_id": "TEST-100", "quantity": 1, "unit_price": 50.0}
    ]
    
    resp_orden = client.post("/orders/", json=payload, headers=headers)
    
    # 3. Aserciones de integración y lógica de negocio
    assert resp_orden.status_code == 201
    assert resp_orden.json()["total_amount"] == 50.0
    assert resp_orden.json()["status"] == "PENDING"