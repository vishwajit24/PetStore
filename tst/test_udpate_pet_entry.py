import pytest
import json
from pet_store_operations.pet_store_operation import PetStoreOperation
from tst.utils import create_pet_entry_data, check_results, randomly_provide_status, create_random_string_inputs, \
    create_random_int_inputs, create_json_input_for_tags_category

pet_store_operation = PetStoreOperation()


@pytest.mark.timeout(60)
def test_updating_pet_entry():
    pet_id = create_random_int_inputs()
    test_data = create_pet_entry_data(pet_id=pet_id,
                                      pet_name=create_random_string_inputs(),
                                      pet_photo=[create_random_string_inputs()],
                                      pet_status=randomly_provide_status())
    response = pet_store_operation.create_pet_entry(payload=test_data)
    assert response.status_code == 200
    new_test_data = create_pet_entry_data(pet_id=pet_id,
                                      pet_name=create_random_string_inputs(),
                                      pet_photo=[create_random_string_inputs()],
                                      pet_status=randomly_provide_status())
    updated_response = pet_store_operation.update_pet_entry(payload=test_data)
    assert updated_response.status_code == 200
    updated_response = json.loads(updated_response.text)
    check_results(new_test_data, updated_response)


@pytest.mark.timeout(60)
def test_update_entry_with_invalid_data():
    pet_id = create_random_int_inputs()
    test_data = create_pet_entry_data(pet_id=pet_id,
                                      pet_name=create_random_string_inputs(),
                                      pet_photo=[create_random_string_inputs()],
                                      pet_status=randomly_provide_status())
    updated_response = pet_store_operation.update_pet_entry(payload=test_data)
    assert updated_response.status_code == 200
    updated_response = json.loads(updated_response.text)
    check_results(test_data, updated_response)

