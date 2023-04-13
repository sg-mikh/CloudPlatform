from framework.api.client import Client


class ProductInventory(Client):

    def get_projects(self):
        """
        Получение списка проектов. Есть Фильтр по облаку: ?cloud_id={cloud_id}
        и фильтр по департаменту: ?ou_id={ou_id}
        """
        return Client._s.get(Client.host + "api/product-inventory/v1/projects", verify=False)

    def get_project(self, id: str):
        """
        Получение данных проекта по ID
        """
        return Client._s.get(Client.host + f"api/product-inventory/v1/projects/{id}", verify=False)

    def post_projects(self, json: dict):
        """
        Создание проекта
        """
        return Client._s.post(Client.host + "api/product-inventory/v1/projects", json=json, verify=False)

    def patch_projects_id(self, id: str, json: dict):
        """
        Обновление проекта
        """
        return Client._s.patch(Client.host + f"api/product-inventory/v1/projects/{id}", json=json, verify=False)

    def delete_projects_id(self, id: str):
        """
        Удаление проекта
        """
        return Client._s.delete(Client.host + f"api/product-inventory/v1/projects/{id}", verify=False)

    def get_products(self, project_id: str):
        """
        Получение списка подключенных продуктов в проекте
        """
        return Client._s.get(Client.host + f"api/product-inventory/v1/product-instances?project_id={project_id}"
                                           f"&status=active", verify=False)

    # МЕТОД НЕ РЕАЛИЗОВАН
    # def get_product(self, id: str):
    #     """
    #     Получение продукта по ID
    #     """
    #     return Client._s.get(Client.host + f"/product-inventory/v1/product-instances?{id}", verify=False)
    # НЕДОСТУПНЫ ПО REST СНАРУЖИ
    # 2 сервиса
