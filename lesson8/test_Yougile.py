import requests
import pytest

base_url = "https://yougile.com/api-v2"

my_key = "0wkOclDgg0BcEh2FHbTYmouKu+mBlDRaNz0qkDpYOD75WJMS7KTOKcSQamGN-eEK"
Authorization = f'Bearer {my_key}'
my_headers = {
    'Content-Type': 'application/json',
    'Authorization': Authorization
    }
id_employees = 'b3de5e2f-c6d1-45a7-b3f7-2b6f6ea68b27'


#  Тест. Создание проекта.
# @pytest.mark.positive_test
def test_positive_create_project():
    body = {
        'title': 'project #1 от 17/03/25',
        'users': {id_employees: 'admin'}
    }
    resp = requests.post(base_url + '/projects',
                         json=body,
                         headers=my_headers)
    project_id = resp.json()['id']
    assert resp.status_code == 201
    assert body['title'] == 'project #1 от 17/03/25'
    assert body['users'][id_employees] == 'admin'
    assert 'application/json' in resp.headers['Content-Type']


#  Тест. Создание проекта (проверка длинны списка).
# @pytest.mark.positive_test
def test_create_project_len():
    # получить список проектов
    len_projects = requests.get(base_url + '/projects',
                                headers=my_headers)
    len_projects_data = len_projects.json().get("content", [])
    assert len_projects.status_code == 200
# создать проект
    body = {
        'title': 'project #1 от 17/03/25',
        'users': {'b3de5e2f-c6d1-45a7-b3f7-2b6f6ea68b27': 'admin'}
    }
    resp = requests.post(base_url + '/projects',
                         json=body,
                         headers=my_headers)
    assert body['title'] == 'project #1 от 17/03/25'
    assert resp.status_code == 201
# повторно получить список проектов
    full_len_projects = requests.get(base_url + '/projects',
                                     headers=my_headers)
    full_len_projects_data = full_len_projects.json().get("content", [])
    assert full_len_projects.status_code == 200
# сравнить первый и второй списки
    assert len_projects_data < full_len_projects_data


#  Тест. Создание проекта.
# @pytest.mark.negative_test
def test_negative_create_project():
    body = {
        'title': '',
        'users': {id_employees: 'admin'}
    }
    resp = requests.post(base_url + '/projects',
                         json=body,
                         headers=my_headers)
    assert resp.status_code == 400
    assert resp.json()["message"] == ["title should not be empty"]


# Тест. Изменить проект.
# @pytest.mark.positive_test
def test_positive_modify_project():
    body = {
        'title': 'project #1 от 16/03/25',
        'users': {id_employees: 'admin'}
    }
    resp = requests.post(base_url + '/projects',
                         json=body,
                         headers=my_headers)
    project_id = resp.json()['id']

    body = {
        'title': 'project #2 от 18/03/25',
        'users': {id_employees: 'admin'}
    }
    resp = requests.put(base_url + '/projects/' + project_id,
                        json=body,
                        headers=my_headers)
    assert resp.status_code == 200


# Тест. Изменить проект.
# @pytest.mark.negative_test
def test_negative_id_modify_project():
    body = {
        'title': 'project #1 от 16/03/25',
        'users': {id_employees: 'admin'}
    }
    resp = requests.post(base_url + '/projects',
                         json=body,
                         headers=my_headers)
    project_id = resp.json()['id']

    body = {
        'title': 'project #1 от 117/03/25',
        'users': {'': 'admin'}
    }
    resp = requests.put(base_url + '/projects/' + project_id,
                        json=body,
                        headers=my_headers)
    resp.json()
    assert resp.status_code == 400
    assert resp.json()
    ["message"] == 'Сотрудники со следующими ID не найдены в компании: '


# Тест. Изменить проект.
# @pytest.mark.negative_test
def test_negative_title_modify_project():
    body = {
        'title': 'project #1 от 16/03/25',
        'users': {id_employees: 'admin'}
    }
    resp = requests.post(base_url + '/projects',
                         json=body,
                         headers=my_headers)
    project_id = resp.json()['id']

    body = {
        'title': '',
        'users': {id_employees: 'admin'}
    }
    resp = requests.put(base_url + '/projects/' + project_id,
                        json=body,
                        headers=my_headers)
    resp.json()
    assert resp.status_code == 400
    assert resp.json()["message"] == ["title should not be empty"]


# Тест. Получить ID проекта.
# @pytest.mark.positive_test
def test_positive_get_by_id():
    body = {
        'title': 'project #1 от 16/03/25',
        'users': {id_employees: 'admin'}
    }
    resp = requests.post(base_url + '/projects',
                         json=body,
                         headers=my_headers)
    project_id = resp.json()['id']
    resp = requests.get(base_url + '/projects/' +
                        project_id,
                        headers=my_headers)
    resp.json()
    assert resp.status_code == 200


# Тест. Получить ID проекта (без авторизации).
# @pytest.mark.negative_test
def test_negative_get_by_id():
    body = {
        'title': 'project #1 от 16/03/25',
        'users': {id_employees: 'admin'}
    }
    resp = requests.post(base_url + '/projects',
                         json=body,
                         headers=my_headers)
    project_id = resp.json()['id']
    resp = requests.get(base_url + '/projects/' +
                        '11111111111111111111111111',
                        headers=my_headers)
    resp.json()
    assert resp.status_code == 404
