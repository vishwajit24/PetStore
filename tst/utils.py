import random
import string


def create_pet_entry_data(pet_id, pet_name, pet_photo=[], pet_category={}, pet_tag=[], pet_status=''):
    """
    Example of the structure of the payload to be returned
        {
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
         },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
            "id": 0,
            "name": "string"
            }
        ],
        "status": "available"
        }
    :return: the payload for create_pet_entry_api
    """
    payload = {}
    payload['id'] = pet_id
    if pet_category:
        payload['category'] = {}
        payload['category']['id'] = pet_category['id']
        payload['category']['name'] = pet_category['name']
    payload['name'] = pet_name
    payload['photoUrls'] = pet_photo
    if pet_tag:
        payload['tags'] = pet_tag
    payload['status'] = pet_status
    return payload


def create_random_string_inputs():
    data = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
    return data


def create_random_int_inputs():
    data = random.randint(1, 1000)
    return data


def randomly_provide_status():
    status = ['available', 'pending', 'sold']
    data = random.choice(status)
    return data


def create_json_input_for_tags_category(input_id, input_name):
    data_input = {}
    data_input['id'] = input_id
    data_input['name'] = input_name
    return data_input


def check_results(expected_result, returned_result):

    assert expected_result['id'] == returned_result['id']
    if 'category' in expected_result:
        assert expected_result['category']['id'] == returned_result['category']['id']
        assert expected_result['category']['name'] == returned_result['category']['name']
    assert expected_result['name'] == returned_result['name']
    assert expected_result['photoUrls'].sort() == returned_result['photoUrls'].sort()
    if 'tags' in expected_result:
        assert expected_result['tags'] == returned_result['tags']
    else:
        assert len(returned_result['tags']) == 0
    assert expected_result['status'] == returned_result['status']
