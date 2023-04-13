from framework.api.client import Client


class OrderManager(Client):

    def create_order(self, json: dict, expected_status_code: int):
        """
        Создание заказа
        """
        return Client.post(Client.host + "/order-manager/v1/orders", expected_status_code, json=json)

    def get_order(self, order_id: str, expected_status_code: int):
        """
        Получение заказа
        """
        return Client.get(Client.host + f"/order-manager/v1/orders/{order_id}", expected_status_code)

    def get_orders(self, expected_status_code: int):
        """
        Получение заказов
        """
        return Client.get(Client.host + "/order-manager/v1/orders", expected_status_code)

    def get_tasks(self, expected_status_code: int):
        """
        Получение всех задач
        """
        return Client.get(Client.host + "/order-manager/v1/tasks", expected_status_code)

    def get_task(self, task_id: str, expected_status_code: int):
        """
        Получение задачи
        """
        return Client.get(Client.host + f"/order-manager/v1/tasks/{task_id}", expected_status_code,
                          json_scheme_filename='task.json')
