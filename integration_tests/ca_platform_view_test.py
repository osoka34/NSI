import requests

# pytest integration_tests/ca_platform_view_test.py

BASE_URL = "http://localhost:11000/v1/ca_parameters/view"
def test_get_all_by_id():
    ca_id = 2
    response = requests.get(f"{BASE_URL}/get_all_by_id/{ca_id}")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert len(data["data"]) > 0

def test_get_all():
    response = requests.get(f"{BASE_URL}/get_all")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert len(data["data"]) > 0


