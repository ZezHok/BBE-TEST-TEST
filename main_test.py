import pytest
import requests

#
# Просто пример теста
#
def test_update_pet_data(base_url, update_pet_data):
    update_pet = requests.put(f'{base_url}/pet', json=update_pet_data)

    print('\nUpdate pet data')
    print('Text: ' + update_pet.text)
    print('Status: ' + str(update_pet.status_code))
    assert update_pet.status_code == 200
    print('Headers: ' + str(update_pet.headers))
    assert update_pet.headers['Content-Type'] == 'application/json'

#
# Тест Татьяны
#
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

#
# Тест Татьяны 
#
def test2():
    print("second test")


#
# Тест Наталия 
#

def test_pet_operations(base_url, pet_id):
    # POST: Add a new pet
    pet_data = {
        "id": pet_id,
        "name": "Buddy",
        "category": {"id": 1, "name": "Dogs"},
        "photoUrls": ["https://example.com/photo"],
        "tags": [{"id": 1, "name": "friendly"}],
        "status": "available"
    }
    create_pet = requests.post(f'{base_url}/pet', json=pet_data)
    print("Create pet response: " + create_pet.text)
    assert create_pet.status_code == 200
    assert create_pet.headers['Content-Type'] == 'application/json'

    # PUT: Update the pet
    update_data = {
        "id": pet_id,
        "name": "Buddy",
        "category": {"id": 1, "name": "Dogs"},
        "photoUrls": ["https://example.com/photo"],
        "tags": [{"id": 1, "name": "friendly"}],
        "status": "sold"
    }
    update_pet = requests.put(f'{base_url}/pet', json=update_data)
    print("Update pet response: " + update_pet.text)
    assert update_pet.status_code == 200
    assert update_pet.headers['Content-Type'] == 'application/json'

    # GET: Find pet by ID
    get_pet = requests.get(f'{base_url}/pet/{pet_id}')
    print("Get pet response: " + get_pet.text)
    assert get_pet.status_code == 200
    assert get_pet.headers['Content-Type'] == 'application/json'
    pet_info = get_pet.json()
    assert pet_info['id'] == update_data['id']
    assert pet_info['status'] == update_data['status']

    # JSON Schema validation for GET response
    pet_schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "category": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"}
                },
            },
            "photoUrls": {"type": "array", "items": {"type": "string"}},
            "tags": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "name": {"type": "string"}
                    },
                }
            },
            "status": {"type": "string"}
        },
        "required": ["id", "name", "category", "photoUrls", "tags", "status"]
    }

    try:
        validate(instance=pet_info, schema=pet_schema)
        print("JSON schema validation success.")
    except jsonschema.exceptions.ValidationError as e:
        print("Error validating JSON Schema: ")
        print(e)
        raise e

    # DELETE: Deletes a pet
    delete_pet = requests.delete(f'{base_url}/pet/{pet_id}')
    print("Delete pet response: " + delete_pet.text)
    assert delete_pet.status_code == 200
    assert delete_pet.headers['Content-Type'] == 'application/json'

#
# Тест Наталия 
#

@pytest.mark.parametrize("test_data", [123, 432, 456])
def test_id(test_data):
    assert test_data == 456
    
