import logging
import pytest

from framework.api.microservices.customer_manager import CustomerManager, AdminCustomerManager
from framework.testdata import users

logger = logging.getLogger(__name__)


# Создание\просмотр\редактирование\удаление департаментов
# @allure.label("Jira", "CP-143")
class TestAdminCustomerManager:

    def test_get_admin_customers(self):
        response = AdminCustomerManager.get_admin_customers(self, expected_status_code=200)
        logger.info(response.json())
        logger.info(response.status_code)
        logger.info(response.reason)

    def test_get_admin_customer(self):
        response = AdminCustomerManager.get_admin_customer(self, "497fcf40-e10a-417d-a8bc-41b3f737a1ce",
                                                           expected_status_code=200)
        logger.info(response.json())
        logger.info(response.status_code)
        logger.info(response.reason)

    def test_patch_admin_customer(self):
        response = AdminCustomerManager.patch_admin_customer(self, "2117e508-d285-4e75-9e5a-485949229fbb",
                                                           expected_status_code=200)
        logger.info(response.json())
        logger.info(response.status_code)
        logger.info(response.reason)

    @pytest.mark.skip(reason="работает некорректно")
    def test_get_admin_search_customer(self):
        response = AdminCustomerManager.get_admin_search_customer(self, limit=10, page=10, type="LEGAL",
                                                                  expected_status_code=200)
        logger.info(response.json())
        logger.info(response.status_code)
        logger.info(response.reason)


class TestCustomerManager:

    def test_get_me(self):
        response = CustomerManager.get_me(self, users.MLSpaceUser, expected_status_code=200)
        logger.info(response.json())
        logger.info(response.status_code)
        logger.info(response.reason)
