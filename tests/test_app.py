

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_predict_response():
    response = client.post("/predict", json={
        "Warehouse_block": 1,
        "Mode_of_Shipment": 0,
        "Customer_care_calls": 4,
        "Customer_rating": 3,
        "Cost_of_the_Product": 200.0,
        "Prior_purchases": 2,
        "Product_importance": 1,
        "Gender": 1,
        "Discount_offered": 10.0,
        "Weight_in_gms": 2500.0
    })
    assert response.status_code == 200
    assert response.json()["prediction"] in ["On-Time", "Delayed"]

def test_dummy():
    assert 1 == 1

