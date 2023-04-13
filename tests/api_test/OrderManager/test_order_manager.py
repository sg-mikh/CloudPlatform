import logging
import os
import pytest

from pathlib import Path
from framework.api.microservices.order_manager import OrderManager
from framework.helpers.common import get_json

logger = logging.getLogger(__name__)
task_id = "19f85c68-f5e8-49e2-ac26-c17ab33c7b2a"
order_id = "25159794-c58e-456a-bc0c-06774dcd1bc7"
path = Path(os.path.abspath(os.path.dirname(os.path.abspath(__file__))))


class TestOrderManager:

    @pytest.mark.skip(reason="нужно подготовить тестовые данные")
    def test_post_order(self):
        response = OrderManager.create_order(self, expected_status_code=200,
                                             json=get_json(f'{path}/order_to_create.json'))
        logger.info(response.json())

    def test_get_order(self):
        response = OrderManager.get_order(self, order_id, expected_status_code=200)
        logger.info(response.json())

    @pytest.mark.skip(reason="ручка не работает, возможно только по grpc")
    def test_get_orders(self):
        response = OrderManager.get_orders(self, expected_status_code=200)
        logger.info(response.json())

    def test_get_tasks(self):
        response = OrderManager.get_tasks(self, expected_status_code=200)
        logger.info(response.json())

    def test_get_task(self):
        response = OrderManager.get_task(self, task_id, expected_status_code=200)
        logger.info(response.json())
