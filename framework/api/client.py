# -*- coding: utf-8 -*-
import logging
import requests

from framework.helpers import common
from framework.testdata.users import BaseProductUser, MLSpaceUser

logger = logging.getLogger(__name__)


class Client:
    """
    Класс описывающий работу с REST API платформы
    """
    _s = requests.session()
    host = 'https://console-dev.cf/api'
    product_user = MLSpaceUser

    def __init__(self, host, product_user):
        self.host = host
        self.product_user = product_user

    @staticmethod
    def get_token(product_user: BaseProductUser):
        data = {
            "client_id": "cloud_platform_services",
            "client_secret": "40f18155-09aa-4346-9e0e-0fef2d38a8c7",
            "username": product_user.login,
            "password": product_user.password,
            # "grant_type": "client_credentials",
            "grant_type": "password"
        }
        token = requests.post('https://test.iam.rnd.4cloud.cf/'
                              'auth/realms/master/protocol/openid-connect/token',
                              data=data).json()["access_token"]
        return token

    def authorize(self):
        token = self.get_token()
        self._s.headers.update({'User-Agent': 'Autotest'})
        self._s.headers.update({'Authorization': f'Bearer {token}'})

    @staticmethod
    def get(url: str, expected_status_code: int, timeout: int = 5, json_scheme_filename: str = None):
        """
        Обертка для метода requests.get

        :param expected_status_code: Ожидаемый код ответа
        :rtype: requests.Response
        :param url: URL запроса
        :param timeout: timeout запроса в секундах, по умолчанию 5
        :param json_scheme_filename: JSON схема для ответа на запрос, необязательна
        :return: Ответ на запрос
        """
        Client.log_request('GET', url)
        response = requests.get(url=url, headers=Client.get_header(), timeout=timeout)
        Client.log_response(response)
        assert response.status_code == expected_status_code
        if json_scheme_filename is not None and expected_status_code == 200:
            common.assertion(response, json_scheme_filename)
        else:
            logger.info(f'***** Response JSON schema was not validated for '
                        f'{response.request.method} to {response.request.path_url} *****')
        return response

    @staticmethod
    def post(url: str, expected_status_code: int, timeout: int = 5, json_scheme_filename: str = None,
             json: dict = None):
        """
        Обертка для метода requests.post

        :param expected_status_code: Ожидаемый код ответа, по умолчанию None
        :param json: JSON отправляемые на endpoint
        :rtype: requests.Response
        :param url: URL запроса
        :param timeout: timeout запроса в секундах, по умолчанию 5
        :param json_scheme_filename: JSON схема для ответа на запрос, необязательна
        :return: Ответ на запрос
        """
        Client.log_request('POST', url, json)
        response = requests.post(url=url, headers=Client.get_header(),
                                 json=json, timeout=timeout)
        Client.log_response(response)
        assert response.status_code == expected_status_code
        if json_scheme_filename is not None and expected_status_code is not None:
            common.assertion(response, json_scheme_filename)
        else:
            logger.info(f'Response JSON schema was not validated for '
                        f'{response.request.method} to {response.request.path_url}')
        return response

    @staticmethod
    def patch(url: str, expected_status_code: int, json: dict = None, timeout: int = 5,
              json_scheme_filename: str = None):
        """
        Обертка для метода requests.patch

        :param expected_status_code: Ожидаемый код ответа, по умолчанию None
        :param json: JSON отправляемые на endpoint
        :rtype: requests.Response
        :param url: URL запроса
        :param timeout: timeout запроса в секундах, по умолчанию 5
        :param json_scheme_filename: JSON схема для ответа на запрос, необязательна
        :return: Ответ на запрос
        """
        Client.log_request('PATCH', url, json)
        response = requests.patch(url=url, headers=Client.get_header(),
                                  json=json, timeout=timeout)
        Client.log_response(response)
        assert response.status_code == expected_status_code
        if json_scheme_filename is not None and expected_status_code is not None:
            common.assertion(response, json_scheme_filename)
        else:
            logger.info(f'Response JSON schema was not validated for '
                        f'{response.request.method} to {response.request.path_url}')
        return response

    @staticmethod
    def put(url: str, expected_status_code: int, timeout: int = 5, json_scheme_filename: str = None,
            json: dict = None):
        """
        Обертка для метода requests.patch

        :param expected_status_code: Ожидаемый код ответа, по умолчанию None
        :param json: JSON отправляемые на endpoint
        :rtype: requests.Response
        :param url: URL запроса
        :param timeout: timeout запроса в секундах, по умолчанию 5
        :param json_scheme_filename: JSON схема для ответа на запрос, необязательна
        :return: Ответ на запрос
        """
        Client.log_request('PATCH', url, json)
        response = requests.put(url=url, headers=Client.get_header(),
                                json=json, timeout=timeout)
        Client.log_response(response)
        assert response.status_code == expected_status_code
        if json_scheme_filename is not None and expected_status_code is not None:
            common.assertion(response, json_scheme_filename)
        else:
            logger.info(f'Response JSON schema was not validated for '
                        f'{response.request.method} to {response.request.path_url}')
        return response

    @staticmethod
    def delete(url: str, expected_status_code: int, timeout: int = 5, json_scheme_filename: str = None,
               json: dict = None):
        """
        Обертка для метода requests.delete

        :param expected_status_code: Ожидаемый код ответа, по умолчанию None
        :param json: JSON отправляемые на endpoint
        :rtype: requests.Response
        :param url: URL запроса
        :param timeout: timeout запроса в секундах, по умолчанию 5
        :param json_scheme_filename: JSON схема для ответа на запрос, необязательна
        :return: Ответ на запрос
        """
        Client.log_request('DELETE', url, json)
        response = requests.delete(url=url, headers=Client.get_header(),
                                   json=json, timeout=timeout)
        Client.log_response(response)
        assert response.status_code == expected_status_code
        if json_scheme_filename is not None and expected_status_code is not None:
            common.assertion(response, json_scheme_filename)
        else:
            logger.info(f'Response JSON schema was not validated for '
                        f'{response.request.method} to {response.request.path_url}')
        return response

    @staticmethod
    def get_header():
        """
        Метод для формирования header'ов запроса с токеном аутентификации
        и User-agent'ом

        :rtype: dict
        :return: Готовый header для requests запроса
        """
        return {'User-Agent': 'Autotest',
                'Authorization': 'Bearer ' + Client.get_token(Client.product_user)}

    @staticmethod
    def log_request(request_method, url: str, payload=None):
        logger.debug(f"Request: {request_method} {url}")
        if payload is not None:
            logger.debug(f"Request body: {payload}")

    @staticmethod
    def log_response(response: requests.Response):
        logger.debug(f"Response status code: {response.status_code}")
        logger.debug(f"Response reason: {response.reason}")
        logger.debug(f"Response body: {response.text}")
        logger.debug(f"Time to Response: {response.elapsed.total_seconds()}")
