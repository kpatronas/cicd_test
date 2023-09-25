import pytest
from fastapi.testclient import TestClient
from main import app  # Import your FastAPI app

# Create a TestClient instance for testing
client = TestClient(app)

def test_add_numbers():
    # Test adding two numbers
    response = client.get("/add?num1=5.5&num2=3.3")
    assert response.status_code == 200
    assert response.json() == {"result": 8.8}

    # Test adding two different numbers
    response = client.get("/add?num1=10&num2=20")
    assert response.status_code == 200
    assert response.json() == {"result": 30}

    # Test adding zero to a number
    response = client.get("/add?num1=7&num2=0")
    assert response.status_code == 200
    assert response.json() == {"result": 7}

    # Test adding negative numbers
    response = client.get("/add?num1=-2&num2=-5")
    assert response.status_code == 200
    assert response.json() == {"result": -7}

def test_invalid_input():
    # Test invalid input (non-numeric values)
    response = client.get("/add?num1=abc&num2=def")
    assert response.status_code == 421  # Expect a validation error
