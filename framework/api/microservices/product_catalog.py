from framework.api.client import Client


class ProductCatalog(Client):

    #################
    #   Category    #
    #################

    def create_category(self, json: dict):
        """
        Информация о ...#name в json - обязательно
        """
        print("create category")
        return Client._s.post(Client.host + "/product-catalog/api/v1/categories", json=json, verify=False)

    def get_all_categories(self):
        """
        Информация о ...
        """
        print("get categories")
        return Client._s.get(Client.host + "/product-catalog/api/v1/categories", verify=False)

    def get_category(self, id: str):
        """
        Информация о ...
        """
        print("get category")
        return Client._s.get(Client.host + f"/product-catalog/api/v1/categories/{id}", verify=False)

    def update_category(self, id: str, json: dict):
        """
        Информация о ... #name в json - обязательно
        """
        print("update category")
        return Client._s.put(Client.host + f"/product-catalog/api/v1/categories/{id}", json=json, verify=False)

    def delete_category(self, id: str):
        """
        Информация о ...
        для тестирования: если к категории привязан хотя бы один продукт - должна вернуться ошибка удаления
        """
        print("delete category")
        return Client._s.delete(Client.host + f"/product-catalog/api/v1/categories/{id}", verify=False)

    #################
    #   Platform    #
    #################

    def create_platform(self, json: dict):
        """
        Информация о ... #name в json - обязательно
        """
        print("create platform")
        return Client._s.post(Client.host + "/product-catalog/api/v1/platforms", json=json, verify=False)

    def get_all_platforms(self):
        """
        Информация о ...
        """
        print("get platforms")
        return Client._s.get(Client.host + "/product-catalog/api/v1/platforms", verify=False)

    def get_platform(self, id: str):
        """
        Информация о ...
        """
        print("get platform")
        return Client._s.get(Client.host + f"/product-catalog/api/v1/platforms/{id}", verify=False)

    def update_platform(self, id: str, json: dict):
        """
        Информация о ...#name в json - обязательно
        """
        print("update platform")
        return Client._s.put(Client.host + f"/product-catalog/api/v1/platforms/{id}", json=json, verify=False)

    def delete_platform(self, id: str):
        """
        Информация о ...
        для тестирования: если к категории привязан хотя бы один продукт - должна вернуться ошибка удаления
        """
        print("delete platform")
        return Client._s.delete(Client.host + f"/product-catalog/api/v1/platforms/{id}", verify=False)

    #############
    #   Product #
    #############

    def create_product(self, json: dict):
        """
        Информация о ...# в json - обязательно
        name,category_id,platform_id,status,service_id
        """
        print("create category")
        return Client._s.post(Client.host + "/product-catalog/api/v1/products", json=json, verify=False)

    def get_all_products(self):
        """
        Информация о ...
        """
        print("get products")
        return Client._s.get(Client.host + "/product-catalog/api/v1/products", verify=False)

    def get_product(self, id: str):
        """
        Информация о ...
        есть параметры фильтрации
        category_id, platform_id, status
        """
        print("get product")
        return Client._s.get(Client.host + f"/product-catalog/api/v1/products/{id}", verify=False)

    def update_product(self, id: str, json: dict):
        """
        Информация о ... #name в json - обязательно
        """
        print("update category")
        return Client._s.put(Client.host + f"/product-catalog/api/v1/products/{id}", json=json, verify=False)

    def delete_product(self, id: str):
        """
        Информация о ...
        """
        print("delete product")
        return Client._s.delete(Client.host + f"/product-catalog/api/v1/products/{id}", verify=False)

    #################
    #   Offering    #
    #################

    def create_offering(self, json: dict):
        """
        Информация о ...# в json - обязательно
        name,price_components[],product_id_id,status,type, sku
        """
        print("create offering")
        return Client._s.post(Client.host + "/product-catalog/api/v1/offerings", json=json, verify=False)

    def get_all_offerings(self):
        """
        Информация о ... product_id, status
        """
        print("get offerings")
        return Client._s.get(Client.host + "/product-catalog/api/v1/offerings", verify=False)

    def get_offering(self, id: str):
        """
        Информация о ...
        есть параметры фильтрации
        category_id, platform_id, status
        """
        print("get offering")
        return Client._s.get(Client.host + f"/product-catalog/api/v1/offerings/{id}", verify=False)

    def update_offering(self, id: str, json: dict):
        """
        Информация о ... #name в json - обязательно
        """
        print("update offering")
        return Client._s.put(Client.host + f"/product-catalog/api/v1/offerings/{id}", json=json, verify=False)

    def delete_offering(self, id: str):
        """
        Информация о ...
        """
        print("delete offering")
        return Client._s.delete(Client.host + f"/product-catalog/api/v1/offerings/{id}", verify=False)
