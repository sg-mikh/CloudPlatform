from framework.api.client import Client


class ServiceInventory(Client):

    def get_service_instance_data(self, id: str):
        """
        Получение данных service instance по его ID
        """
        return Client._s.get(Client.host + f"/service-inventory/v1/service-instances/{id}", verify=False)

    # НЕДОСТУПНЫ ПО REST СНАРУЖИ
    # 8 сервисов
