import pytest
import logging

from framework.api.microservices.iam import IamV2
from framework.testdata import users

logger = logging.getLogger(__name__)
project_id = "d8e26141-4791-4a40-aec7-44f7bf3f7f0b"  # (ML Space'ы)


class TestIamCustomerService:
    #####################
    #   CustomerService #
    #####################

    def test_get_customer_info(self):
        response = IamV2.get_customer_info(self, users.MLSpaceUser.customer_id, expected_status_code=200)
        logger.info(response.json())

    @pytest.mark.skip(reason="ручка не готова")
    def test_get_2fa_status(self):
        response = IamV2.get_2fa_status(self, users.MLSpaceUser.customer_id, expected_status_code=200)
        logger.info(response.json())

    def test_get_folder_list(self):
        response = IamV2.get_folders_list(self, users.MLSpaceUser.customer_id, expected_status_code=200)
        logger.info(response.json())

    def test_get_folder_list_fake_id(self):
        response = IamV2.get_folders_list(self, "1234", expected_status_code=400)
        logger.info(response.json())

    def test_get_permissions_list(self):
        response = IamV2.get_permissions_list(self, users.MLSpaceUser.customer_id, expected_status_code=200)
        logger.info(response.json())

    def test_get_projects_list(self):
        response = IamV2.get_projects_list(self, users.MLSpaceUser.customer_id, expected_status_code=200)
        logger.info(response.json())

    @pytest.mark.skip(reason="ручка не готова")
    def test_get_users_list(self):
        response = IamV2.get_users_list(self, users.MLSpaceUser.customer_id, expected_status_code=200)
        logger.info(response.json())

    def test_add_customer(self):
        response = IamV2.add_customer(self, {
            "customer_id": '2117e508-1112-4e75-9e5a-485949229fbb',
            "display_name": "TEMP-CUSTOMER"
        }, expected_status_code=200)
        logger.info(response.json())
        logger.info(response.status_code)
        logger.info(response.reason)

    def test_update_customer(self):
        response = IamV2.update_customer(self, '2117e508-1112-4e75-9e5a-485949229fbb', {
            "customer_id": "2117e508-1112-4e75-9e5a-485949229fbb",
            "params": {
                "display_name": "123123123"
            }
        }, expected_status_code=200)
        logger.info(response.json())
        logger.info(response.status_code)
        logger.info(response.reason)

    def test_delete_customer(self):
        response = IamV2.delete_customer(self, "2117e508-1112-4e75-9e5a-485949229fbb", expected_status_code=200)
        logger.info(response.json())
        logger.info(response.status_code)
        logger.info(response.reason)
