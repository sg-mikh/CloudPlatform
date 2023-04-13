from framework.api.client import Client


class ServiceOrchestrator(Client):

    def create_service(self, json: dict):
        """
        Создание сервиса в каталоге оркестратора
        """
        return Client._s.post(Client.host + "/service-orchestrator/v1/services", json=json, verify=False)

    # НЕДОСТУПНЫ ПО REST СНАРУЖИ
    # 3 сервиса
