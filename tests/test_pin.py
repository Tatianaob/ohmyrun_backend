import pytest
from app.models.pin import Pin

@pytest.mark.skip(reason="No way to test this feature yet")
def test_get_pin_no_save_pin(client):
    #Act
    response = client.get("/pin")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body == []
