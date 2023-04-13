import pytest
import logging

from framework.api.microservices.iam import IamV2

logger = logging.getLogger(__name__)
project_id = "d8e26141-4791-4a40-aec7-44f7bf3f7f0b"  # (ML Space'ы)


class TestIamMeService:
    #####################
    #     MeService     #
    #####################
    def test_get_me(self):
        response = IamV2.get_me(self, expected_status_code=200)
        logger.info(response.json())
        logger.info(response.status_code)
        logger.info(response.reason)

    @pytest.mark.skip(reason="ручка не готова")
    def test_get_me_context(self, client):
        response = IamV2.get_me_context(self, expected_status_code=200)
        logger.info(response.json())
        logger.info(response.status_code)
        logger.info(response.reason)

    def test_get_me_permissions(self):
        response = IamV2.get_me_permissions(self, expected_status_code=200)
        logger.info(response.json())
        logger.info(response.status_code)
        logger.info(response.reason)

    # @pytest.mark.parametrize('object_type', ['customer', 'folder', 'project', 'resource'])
    def test_get_me_permissions_scopes(self):
        response = IamV2.get_me_permissions_scopes(self, 'project', project_id, expected_status_code=200)
        logger.info(response.json())
        logger.info(response.status_code)
        logger.info(response.reason)
