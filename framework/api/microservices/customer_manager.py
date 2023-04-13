from framework.api.client import Client
from framework.testdata.users import Admin, BaseProductUser


class AdminCustomerManager(Client):

    Client.product_user = Admin

    def get_admin_customers(self, expected_status_code: int):
        """
        Метод возвращает все customer_id
        """
        return Client.get(Client.host + "/customer-manager/v2/admin/customers", expected_status_code)

    def get_admin_search_customer(self, expected_status_code: int, limit: int, page: int, type: str = None,
                                  legal_name: str = None, inn: str = None, first_name: str = None,
                                  last_name: str = None, patronymic: str = None, customer_crm_id: str = None):
        """
        Поиск customer по критериям
        Available type values : TYPE_UNSPECIFIED, LEGAL, INDIVIDUAL, ENTREPRENEUR, NON_RESIDENT
        """
        return Client.get(Client.host + f"/customer-manager/v2/admin/customers/search?limit={limit}&page={page}"
                                        f"&type={type}&legal_name={legal_name}&inn={inn}&first_name={first_name}"
                                        f"&last_name={last_name}&patronymic={patronymic}"
                                        f"&customer_crm_id={customer_crm_id}", expected_status_code)

    def get_admin_customer(self, customer_id: str, expected_status_code: int):
        """
        Метод возвращает информацию о customer
        """
        return Client.get(Client.host + f"/customer-manager/v2/admin/customers/{customer_id}", expected_status_code)

    def post_admin_customer(self, customer_id: str, expected_status_code: int):
        """
        Метод ??
        """
        return Client.post(Client.host + "/customer-manager/v2/admin/customers", expected_status_code)

    def patch_admin_customer(self, customer_id: str, expected_status_code: int):
        """
        Метод обновляет customer только по тем полям, которые были заполнены
        """
        return Client.patch(Client.host + f"/customer-manager/v2/admin/customers/{customer_id}", expected_status_code)


class CustomerManager(Client):
    #####################
    #      Clouds       #
    #####################
    def get_customers_clouds(self, expected_status_code: int):
        """
        Получение списка облаков текущего пользователя
        """
        return Client.get(Client.host + "/customer-manager/v1/clouds", expected_status_code)

    #####################
    #     Customers     #
    #####################
    def get_customer_info(self, customer_id: str, expected_status_code: int):
        """
        Получение данных клиента (организации) по ID
        """
        return Client.get(Client.host + f"/customer-manager/v1/customers/{customer_id}", expected_status_code)

    #####################
    #        OU         #
    #####################
    def get_departments_in_cloud(self, cloud_id: str, expected_status_code: int):
        """
        Получение списка департаментов в облаке
        """
        return Client.get(Client.host + f"/customer-manager/v1/ou?cloud_id={cloud_id}", expected_status_code)

    def get_clouds(self, expected_status_code: int):
        """
        Получение списка департаментов в облаке
        """
        return Client.get(Client.host + f"/customer-manager/v1/ou", expected_status_code)

    def create_dept(self, json: dict):
        """
        Создание департамента. Необходимые поля: "cloud_id","name","description","limit"
        """
        return Client._s.post(Client.host + "/customer-manager/v1/ou", json=json, verify=False)

    def update_dept(self, ou_id: str, json: dict):
        """
        Изменение данных департамента в полях: "name","description","limit"
        """
        return Client._s.put(Client.host + f"/customer-manager/v1/ou/{ou_id}", json=json, verify=False)

    def get_dept(self, id: str):
        """
        Возвращает данные департамента по ID
        """
        return Client._s.get(Client.host + f"/customer-manager/v1/ou/{id}", verify=False)

    def delete_dept(self, ou_id: str):
        """
        Удаление департамента
        """
        return Client._s.delete(Client.host + f"/customer-manager/v1/ou/{ou_id}", verify=False)

    #################
    #       V2      #
    #################
    #####################
    #  CustomerService  #
    #####################
    def get_me(self, product_user: BaseProductUser, expected_status_code: int):
        """
        Метод возвращает информацию о текущем авторизованном customer
        """
        Client.product_user = product_user
        return Client.get(Client.host + "/customer-manager/v2/customers/me", expected_status_code)
