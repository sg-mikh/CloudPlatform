from framework.api.client import Client


class IamV1(Client):

    def get_my_info(self, expected_status_code: int):
        """
        Получение данных профиля
        """
        return Client.get(Client.host + "/iam/v1/users/me", expected_status_code, json_scheme_filename='iam.json')

    def get_user_info(self, id: str, expected_status_code: int):
        """
        Получение данных юзера по ID
        """
        return Client.get(Client.host + f"/iam/v1/users/{id}", expected_status_code, json_scheme_filename='iam.json')

    def get_my_roles(self, expected_status_code: int):
        """
        Получение списка ролей
        """
        return Client.get(Client.host + "/iam/v1/roles", expected_status_code)

    def get_resource_permissions(self, id: str, expected_status_code: int):
        """
        Получение списка прав на ресурс
        :param id: id ресурса (например, проекта)
        """
        return Client.get(Client.host + f"/iam/v1/resources/{id}/permissions", expected_status_code)

    def post_user_roles(self, id: str, json: dict, expected_status_code: int):
        """
        Назначение юзеру роли на ресурс

        :param id: id ресурса (например, проекта)
        """
        return Client._s.post(Client.host + f"iam/v1/users/{id}/permissions", expected_status_code, json=json)

    def delete_user_permissions(self, id: str, expected_status_code: int):
        """
        Удаление роли юзера на ресурс
        """
        return Client._s.delete(Client.host + f"iam/v1/users/{id}/permissions", expected_status_code)

    def create_user(self, json: dict, expected_status_code: int):
        """
        Создание пользователя
        """
        return Client._s.post(Client.host + "iam/v1/users", expected_status_code, json=json)

    def update_user(self, id: str, json: dict, expected_status_code: int):
        """
        Обновление данных пользователя администратором
        """
        return Client._s.put(Client.host + f"iam/v1/users/{id}", expected_status_code, json=json)

    def update_keyclok(self, id: str, json: dict):
        return Client._s.put(f"https://test.iam.rnd.4cloud.cf/auth/admin/realms/master/users/{id}", json=json,
                             verify=False)

    # НЕДОСТУПНЫ ПО REST СНАРУЖИ
    # def post_resource(self):
    #     """
    #     Создание ресурса
    #     """
    #     return Client._s.post(Client.host + f"/iam/v1/resources", verify=False)
    #
    # def get_user_resources(self, id: str):
    #     """
    #     Получение ресурса по ID
    #     """
    #     return Client._s.get(Client.host + f"/iam/v1/resources/{id}", verify=False)
    #
    # def delete_user_resources(self, id: str):
    #     """
    #     Удаление ресурса
    #     """
    #     return Client._s.delete(Client.host + f"/iam/v1/resources/{id}", verify=False)
    #
    # def delete_user(self, id: str):
    #     """
    #     Удаление пользователя
    #     """
    #     return Client._s.delete(Client.host + f"/iam/v1/users/{id}", verify=False)
    #
    # def get_my_permissions(self):
    #     """
    #     Метод для проверки прав доступа
    #     """
    #     return Client._s.get(Client.host + f"/iam/v1/users/access", verify=False)


class IamV2(Client):

    #####################
    #   CustomerService #
    #####################

    def add_customer(self, json: dict, expected_status_code: int):
        """
        Метод добавляет нового заказчика в iam
        """
        return Client.post(Client.host + "/iam/v2/customers", expected_status_code, json=json)

    def get_customer_info(self, customer_id: str, expected_status_code: int):
        """
        Метод возвращает информацию о заказчике
        """
        return Client.get(Client.host + f"/iam/v2/customers/{customer_id}", expected_status_code,
                          json_scheme_filename='customer.json')

    def delete_customer(self, customerId: str, expected_status_code: int):
        """
        Метод удаляет заказчика из iam
        """
        return Client.delete(Client.host + f"/iam/v2/customers/{customerId}", expected_status_code)

    def update_customer(self, customer_id: str, json: dict, expected_status_code: int):
        """
        Метод обновляет информацию о заказчике
        """
        return Client.put(Client.host + f"/iam/v2/customers/{customer_id}", expected_status_code, json=json)

    def get_2fa_status(self, customer_id: str, expected_status_code: int):
        """
        Метод возвращает флаг статуса двухфакторной аутентификации
        """
        return Client.get(Client.host + f"/iam/v2/customers/{customer_id}/2fa", expected_status_code)

    def disable_2fa(self, customer_id: str, expected_status_code: int):
        """
        Метод выключает двухфакторную аутентификацию для всех пользователей связанных с заказчиком
        """
        return Client.put(Client.host + f"/iam/v2/customers/{customer_id}/2fa/disable", expected_status_code)

    def enable_2fa(self, customer_id: str, expected_status_code: int):
        """
        Метод включает двухфакторную аутентификацию для всех пользователей связанных с заказчиком
        """
        return Client.put(Client.host + f"/iam/v2/customers/{customer_id}/2fa/enable", expected_status_code)

    def get_folders_list(self, customer_id: str, expected_status_code: int):
        """
        Метод возвращает перечень каталогов первого уровня связанные с заказчиком
        """
        return Client.get(Client.host + f"/iam/v2/customers/{customer_id}/folders", expected_status_code,
                          json_scheme_filename='folders.json')

    def get_permissions_list(self, customer_id: str, expected_status_code: int):
        """
        Метод возвращает перечень прав выданных на заказчика
        """
        return Client.get(Client.host + f"/iam/v2/customers/{customer_id}/permissions", expected_status_code)

    def get_projects_list(self, customer_id: str, expected_status_code: int):
        """
        Метод возвращает все доступные пользователю проекты в рамках заказчика
        """
        return Client.get(Client.host + f"/iam/v2/customers/{customer_id}/projects", expected_status_code,
                          json_scheme_filename='projects.json')

    def get_users_list(self, customer_id: str, expected_status_code: int):
        """
        Метод возвращает перечень пользователей у которых есть доступ к заказчику или к его объектам
        """
        return Client.get(Client.host + f"/iam/v2/customers/{customer_id}/users", expected_status_code)

    #####################
    #   UserService     #
    #####################

    def get_user_info(self, user_id: str, expected_status_code: int):
        """
        Метод возвращает информацию о пользователе
        """
        return Client.get(Client.host + f"/iam/v2/users/{user_id}", expected_status_code)

    def get_user_context(self, user_id: str, expected_status_code: int):
        """
        Метод возвращает перечень доступных для пользователя действий по отношению к набору объектов одного типа
        """
        return Client.get(Client.host + f"/iam/v2/users/{user_id}/context", expected_status_code)

    def get_user_permissions(self, user_id: str, expected_status_code: int):
        """
        Метод возвращает перечень прав выданных пользователю
        """
        return Client.get(Client.host + f"/iam/v2/users/{user_id}/permissions", expected_status_code)

    def get_user_permissions_scopes(self, user_id: str, object_type: str, object_id: [str], expected_status_code: int):
        """
        Метод возвращает перечень доступных для пользователя действий по отношению к набору объектов одного типа
        """
        return Client.get(Client.host + f"/iam/v2/users/{user_id}/permissions/{object_type}/scopes?objects={object_id}",
                          expected_status_code)

    #####################
    #     MeService     #
    #####################
    def get_me(self, expected_status_code: int):
        """
        Метод возвращает информацию о пользователе указанном в токене
        """
        return Client.get(Client.host + "/iam/v2/users/me", expected_status_code)

    def get_me_context(self, expected_status_code: int):
        """
        Метод возвращает контекст на основе прав выданных текущему пользователю
        """
        return Client.get(Client.host + "/iam/v2/users/me/context", expected_status_code)

    def get_me_permissions(self, expected_status_code: int):
        """
        Метод возвращает перечень прав выданных текущему пользователю
        """
        return Client.get(Client.host + "/iam/v2/users/me/permissions", expected_status_code)

    def get_me_permissions_scopes(self, object_type: str, object_id: str, expected_status_code: int):
        """
        Метод возвр-ет перечень доступных для текущего пользователя действий по отношению к набору объектов одного типа
        """
        return Client.get(Client.host + f"/iam/v2/users/me/permissions/{object_type}/scopes?objects={object_id}",
                          expected_status_code)
