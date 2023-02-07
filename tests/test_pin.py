import pytest
from app.models.pin import Pin
from app import create_app
from app import db

#@pytest.mark.skip(reason="No way to test this feature yet")
def test_get_pin_no_saved_pin(client):
    #Act
    response = client.get("/pin")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body == []


# get pins one save pin 
# @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_pins_one_save_pin(client, one_pin):
    #Act
    response = client.get("/pin")
    response_body = response.get_json()
    
    #Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body == [
        {
            "id": 1,
            "latitude": 47.83,
            "longitude": -122.33,
            "description": "Run around the park"
        }
    ]

# get pins
#@pytest.mark.skip(reason="No way to test this feature yet")
def test_get_three_pins(client, three_pins):
    # Act
    response = client.get("/pin")
    response_body = response.get_json()
    
    # Assert
    assert response.status_code == 200
    assert len(response_body) == 3
    assert response_body == [
        {
            "id": 1,
            "latitude": 12.34, 
            "longitude":56.789, 
            "description":"First random pin from conftest"
        },
        {
            "id": 2,
            "latitude":52.90, 
            "longitude":-100.99, 
            "description":"Second random pin from conftest"
        },
        {
            "id": 3,
            "latitude":-23.8128, 
            "longitude":-16.2842, 
            "description":"Third random pin from conftest"
        }
    ]

# create pin
#@pytest.mark.skip(reason="No way to test this yet")
def test_create_pin(client):
    #Act
    response = client.post("/pin", json={
        "latitude": 47.83,
        "longitude": -122.33,
        "description": "Running is fun",
    })
    response_body = response.get_json()

    #Assert
    assert response.status_code == 201
    assert response_body == [
        {
         "id": 1,
        "description": "Running is fun",
        "latitude": 47.83,
        "longitude": -122.33,
        }
    ]
    new_pin = Pin.query.get(1)
    assert new_pin.latitude == 47.83
    assert new_pin.longitude == -122.33
    assert new_pin.description == "Running is fun"


# delete pin
#@pytest.mark.skip(reason="No way to test this feature yet")
def test_delete_pin(client, one_pin):
    # Act
    response = client.delete("/pin/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert "details" in response_body
    assert response_body == {
        "details": "Pin successfully deleted"
    }
    assert Pin.query.get(1) == None




