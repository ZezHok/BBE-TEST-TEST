import pytest
import requests

def test_update_pet_data(base_url, update_pet_data):
    update_pet = requests.put(f'{base_url}/pet', json=update_pet_data)

    print('\nUpdate pet data')
    print('Text: ' + update_pet.text)
    print('Status: ' + str(update_pet.status_code))
    assert update_pet.status_code == 200
    print('Headers: ' + str(update_pet.headers))
    assert update_pet.headers['Content-Type'] == 'application/json'


@pytest.mark.regression
def test_pet_operations(base_url, pet_id):

    update_data = {
        "id": pet_id,
        "category": {
            "id": 4,
            "name": "testname"
        },
        "name": "lusia",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
            "id": 6,
            "name": "testtag"
            }
        ],
        "status": "sold"
    }

    update_pet = requests.put(f"{base_url}/pet", json=update_data)
    print("Update pet" + update_pet.text)
    assert update_pet.status_code == 200
    print(update_pet.headers)
    assert update_pet.headers['Content-Type'] == 'application/json'

def test2():
    print("second test")
    
