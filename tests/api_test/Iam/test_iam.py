import pytest
import logging

from framework.api.microservices.iam import IamV1
from framework.testdata import users

logger = logging.getLogger(__name__)
project_id = "d8e26141-4791-4a40-aec7-44f7bf3f7f0b"  # (ML Space'ы)


class TestIam:

    def test_get_my_info(self):
        response = IamV1.get_my_info(self, expected_status_code=200)
        logger.info(response.json())

    @pytest.mark.skip(reason="подобрать пользоватлея который не в своей организации")
    def test_get_user_info_v1(self):
        response = IamV1.get_user_info(self, users.MLSpaceUser.user_id, expected_status_code=200)
        logger.info(response.json())

    @pytest.mark.skip(reason="403 RBAC: access denied")
    def test_get_my_roles(self):
        response = IamV1.get_my_roles(self, expected_status_code=200)
        logger.info(response.json())

    @pytest.mark.skip(reason="подобрать проект данного пользователя")
    def test_get_resource_permissions(self):
        response = IamV1.get_resource_permissions(self, project_id, expected_status_code=200)
        logger.info(response.json())
