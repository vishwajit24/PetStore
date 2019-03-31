import json
import pytest

from pet_store_operations.pet_store_operation import PetStoreOperation
from tst.utils import create_random_int_inputs, create_pet_entry_data, create_random_string_inputs, \
    randomly_provide_status, check_results

pet_store_operation = PetStoreOperation()


@pytest.mark.timeout(60)
def test_getting_created_entry():
    pet_id = create_random_int_inputs()
    test_data = create_pet_entry_data(pet_id=pet_id,
                                      pet_name=create_random_string_inputs(),
                                      pet_photo=[create_random_string_inputs()],
                                      pet_status=randomly_provide_status())
    response = pet_store_operation.create_pet_entry(payload=test_data)
    assert response.status_code == 200
    response = pet_store_operation.get_pet_entry(pet_id)
    assert response.status_code == 200
    response = json.loads(response.text)
    check_results(test_data, response)


@pytest.mark.timeout(60)
def test_getting_non_existing_entry():
    pet_id = create_random_int_inputs()
    response = pet_store_operation.get_pet_entry(pet_id)
    assert response.status_code == 404
    response = json.loads(response.text)
    assert response['message'] == "Pet not found"
    assert response['type'] == "error"
    assert response['code'] == 1


@pytest.mark.timeout(60)
def test_sending_invalid_input():
    pet_id = create_random_int_inputs()
    response = pet_store_operation.get_pet_entry(pet_id)
    assert response.status_code == 404


@pytest.mark.timeout(60)
def test_sending_empty_input():
    response = pet_store_operation.get_pet_entry(pet_id='')
    assert response.status_code == 405
