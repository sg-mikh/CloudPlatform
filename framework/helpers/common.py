import json
import requests
from os.path import join
from jsonschema import validate


def get_json(filename):
    """
    Вернет JSON из файла с указанным именем из папки

    :param filename: Имя файла
    :return: JSON dict
    """
    path = f'{filename}'
    # path = f'./framework/api/microservices/schemas/{filename}'
    # relative_path = Path(os.path.abspath(os.path.dirname(os.path.abspath(__file__)))).parent
    # file_path = relative_path.joinpath(path)
    # return json.load(open(file_path, encoding='utf-8'))
    return json.load(open(path, encoding='utf-8'))


def assert_valid_schema(data, schema_file):
    """Проверка данных на соответствие схеме"""
    schema = _load_json_schema(schema_file)
    return validate(data, schema)


def _load_json_schema(filename):
    """ Загрузка файла со схемой """
    relative_path = join('schemas', filename)
    absolute_path = join('./framework/api', relative_path)
    with open(absolute_path) as schema_file:
        return json.loads(schema_file.read())


def assertion(response: requests.Response, json_filename: str, content_type: str = 'application/json'):
    """
    Метод проверки ответа на запрос

    :param content_type: content type
    :param response: Ответ на запрос
    :param json_filename: Имя файла JSON схемы
    """
    assert response.headers['content-type'] == content_type
    try:
        json_data = response.json()
        assert_valid_schema(json_data, json_filename)
    except AssertionError as err:
        raise err
