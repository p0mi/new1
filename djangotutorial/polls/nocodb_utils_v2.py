import requests
from django.conf import settings

def get_users(table_id):
    url = f'{settings.NOCODB_BASE_URL}tables/{table_id}/records'
    headers = {'xc-token': settings.NOCODB_API_KEY}
    params = {'limit': 25}  # Можно задать другие параметры запроса
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Ошибка при получении данных: {response.text}')