import requests


def request_get(method: str, **params):
    """Returns dict from response"""
    useragent = None
    proxy = None

    data = {
        'access_token': os.getenv(TOKEN),
        'v': 5.131
    }
    data.update(params)

    url = f'https://api.vk.com/method/{method}'

    resp_json = requests.get(url, params=data, headers=useragent, proxies=proxy).json()

    if 'error' in resp_json:
        return resp_json['error']
    else:
        return resp_json['response']


def get_id_from_url(url: str) -> int:
    return request_get('users.get', user_ids=url.split('/')[-1])[0]['id']  # получение id из ссылки


def get_url_from_id(user_id: int) -> str:
    return f'https://vk.com/id{user_id}'


def get_shadows_friends_ids(target_id: int) -> list:
    """Returns list of shadow friends"""

    response = request_get('friends.get', user_id=target_id)  # получение списка друзей

    if 'error_code' in response:
        return []

    results = []

    for i in response['items']:
        friends_friend = request_get("friends.get", user_id=i)
        if 'error_code' in friends_friend:
            continue
        friends_friend = friends_friend['items']
        if target_id not in friends_friend:
            results.append(i)

    return results
