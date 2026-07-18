from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_prediction_success(valid_payload):

    response = client.post(
        "/predict",
        json=valid_payload
    )

    assert response.status_code == 200

    data = response.json()

    assert "predicted_calories" in data
    assert isinstance(data["predicted_calories"], float)
    assert data["predicted_calories"] >= 0


def test_prediction_for_female(valid_payload):

    payload = valid_payload.copy()
    payload["gender"] = "female"

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert set(data.keys()) == {"predicted_calories"}
    assert isinstance(data["predicted_calories"], float)
    assert data["predicted_calories"] >= 0


def test_invalid_gender(valid_payload):

    payload = valid_payload.copy()
    payload["gender"] = "robot"

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 422


def test_negative_age(valid_payload):

    payload = valid_payload.copy()
    payload["age"] = -5

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 422


def test_zero_height(valid_payload):

    payload = valid_payload.copy()
    payload["height"] = 0

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 422


def test_missing_required_field(valid_payload):

    payload = valid_payload.copy()
    del payload["weight"]

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 422


def test_invalid_data_type(valid_payload):

    payload = valid_payload.copy()
    payload["age"] = "twenty"

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 422