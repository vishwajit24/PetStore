import json
import pytest

from pet_store_operations.pet_store_operation import PetStoreOperation
from tst.utils import create_pet_entry_data, create_random_int_inputs, create_random_string_inputs, \
    randomly_provide_status

pet_store_operation = PetStoreOperation()


@pytest.mark.timeout(60)
def test_deleting_existing_pet_entry():
    pet_id = create_random_int_inputs()
    test_data = create_pet_entry_data(pet_id=pet_id,
                                      pet_name=create_random_string_inputs(),
                                      pet_photo=[create_random_string_inputs()],
                                      pet_status=randomly_provide_status())
    pet_store_operation.create_pet_entry(payload=test_data)
    response = pet_store_operation.delete_pet_entry(pet_id)
    assert response.status_code == 200
    response = pet_store_operation.get_pet_entry(pet_id)
    assert response.status_code == 404
    response = json.loads(response.content)
    assert response['message'] == "Pet not found"
    assert response['type'] == "error"


@pytest.mark.timeout(60)
def test_deleting_non_existing_pet_entry():
    pet_id = create_random_int_inputs()
    response = pet_store_operation.delete_pet_entry(pet_id)
    assert response.status_code == 404


@pytest.mark.timeout(60)
def test_deleting_invalid_entry():
    pet_id = create_random_string_inputs()
    response = pet_store_operation.delete_pet_entry(pet_id)
    assert response.status_code == 404

