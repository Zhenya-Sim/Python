import requests

BaseUrl = "https://ru.yougile.com/api-v2/"
company_id = None
token = None
project_id = None


def get_company_id(login='логин',
                   password='пароль', company_name='Поток_QA_100.2'):
    creds = {
            'login': login,
            'password': password,
            'name': company_name
        }
    headers = {
            'Content-Type': 'application/json'
        }
    resp = requests.post(BaseUrl+'auth/companies', json=creds, headers=headers)
    company_id = resp.json()['content'][0]['id']
    return company_id


def get_token(login='логин',
              password='пароль', new_id=company_id):
    new_id = get_company_id()
    creds = {
            'login': login,
            'password': password,
            'companyId': new_id
        }
    headers = {
            'Content-Type': 'application/json'
        }
    resp = requests.post(BaseUrl+'auth/keys', json=creds, headers=headers)
    token = resp.json()['key']
    return token


def test_create_project():
    new_token = get_token()
    headers = {
        'Authorization': f'Bearer {new_token}',
        'Content-Type': 'application/json'
    }
    # не указываем название проекта
    body = {
        'title': '',
        'users': {'4b1ff891-a301-4b07-9594-90f9c5e06701': 'admin'}
    }
    resp = requests.post(BaseUrl+'projects', json=body, headers=headers)
    assert resp.status_code == 400


def test_change_project():
    # создание проекта (если вдруг список пуст)
    new_token = get_token()
    headers = {
        'Authorization': f'Bearer {new_token}',
        'Content-Type': 'application/json'
    }
    body = {
        'title': 'Project3',
        'users': {'4b1ff891-a301-4b07-9594-90f9c5e06701': 'admin'}
    }
    # неверный метод
    resp = requests.post(BaseUrl+'projects', json=body, headers=headers)
    project_id = resp.json()['id']

    # редактирование этого проекта
    new_body = {
        'deleted': False,
        'title': 'Project2',
        'users': {'4b1ff891-a301-4b07-9594-90f9c5e06701': 'admin'}
    }
    result = requests.post(
        BaseUrl+'projects/'+str(project_id), json=new_body, headers=headers)
    assert result.status_code == 404


def test_get_by_id():
    # создание проекта (если вдруг список пуст)
    new_token = get_token()
    headers = {
        'Authorization': f'Bearer {new_token}',
        'Content-Type': 'application/json'
    }
    body = {
        'title': 'Project3',
        'users': {'4b1ff891-a301-4b07-9594-90f9c5e06701': 'admin'}
    }
    resp = requests.post(BaseUrl+'projects/', json=body, headers=headers)
    project_id = resp.json()['id']

    # получить проект по id
    result = requests.get(BaseUrl+'projects/'+project_id)
    assert result.status_code == 401
