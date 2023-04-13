import pytest
import logging

from framework.api.microservices.iam import IamV2
from framework.testdata import users

logger = logging.getLogger(__name__)
project_id = "d8e26141-4791-4a40-aec7-44f7bf3f7f0b"  # (ML Space'ы)


class TestIamUserService:
    #####################
    #   UserService     #
    #####################

    def test_get_user_info_v2(self):
        response = IamV2.get_user_info(self, users.MLSpaceUser.user_id, expected_status_code=200)
        logger.info(response.json())
        logger.info(response.status_code)
        logger.info(response.reason)

    @pytest.mark.skip(reason="ручка не готова")
    def test_get_user_context(self):
        response = IamV2.get_user_context(self, users.MLSpaceUser.user_id, expected_status_code=200)
        logger.info(response.json())
        logger.info(response.status_code)
        logger.info(response.reason)

    def test_get_user_permissions(self):
        # вызов роли
        response = IamV2.get_user_permissions(self, users.MLSpaceUser.user_id, expected_status_code=200)
        logger.info(response.json())
        logger.info(response.status_code)
        logger.info(response.reason)

    # @pytest.mark.parametrize('object_type', ['customer', 'folder', 'project', 'resource'])
    def test_get_user_permissions_scopes(self):
        response = IamV2.get_user_permissions_scopes(self, users.MLSpaceUser.user_id, 'project', project_id,
                                                     expected_status_code=200)
        logger.info(response.json())
        logger.info(response.status_code)
        logger.info(response.reason)
