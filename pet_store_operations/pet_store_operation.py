import logging
import requests
import json

logging.basicConfig(level=logging.INFO)


class PetStoreOperation(object):

    def __init__(self):
        self.url = 'http://petstore.swagger.io/v2/pet'
        self.headers = {
            'Content-type': 'application/json',
            'api_key': 'special-key'
        }

    def get_pet_entry(self, pet_id):

        logger = logging.getLogger("get_pet_entry")

        url = self.url + '/' + str(pet_id)

        try:
            logger.info("Getting the pet_entry with id %s" % pet_id)
            response = requests.get(url=url, headers=self.headers)
            logger.info("Response content: %r", response.content)
            return response
        except Exception as e:
            logger.error("Error occurred while getting the pet entry %r" % e)
            raise e

    def delete_pet_entry(self, pet_id):

        logger = logging.getLogger("delete_pet_entry")

        url = self.url + '/' + str(pet_id)

        try:
            logger.info("Deleting the pet_entry with id %s" % pet_id)
            response = requests.delete(url, headers=self.headers)
            logger.info("Response content: %r", response.content)
            return response
        except Exception as e:
            logger.error("Error occurred while deleting the pet entry %r" % e)
            raise e

    def create_pet_entry(self, payload):

        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger("create_pet_entry")

        payload = json.dumps(payload)
        logger.info("Sending the payload with data %r" % payload)
        try:
            response = requests.post(self.url, data=payload, headers=self.headers)
            logger.info("Response content: %r", response.content)
            return response
        except Exception as e:
            logger.error("Error occurred while calling the create_pet_entry api %s" % e)
            raise e

    def update_pet_entry(self, payload):

        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger("update_pet_entry")

        payload = json.dumps(payload)
        try:
            response = requests.put(url=self.url, data=payload, headers=self.headers)
            logger.info("Response %r", response.content)
            return response
        except Exception as e:
            logger.error("Error occurred while deleting the pet entry %r" % e)
            raise e
