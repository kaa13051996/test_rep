import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta


def calc_age(uid):
    '''
    https://www.coursera.org/learn/python-for-web/programming/POfZx/praktika-po-requests
    Example url: https://api.vk.com/method/users.get?user_id={uid}&v=5.52&access_token={ACCESS_TOKEN}
    :param uid: user id vk.
    :return: A list of pairs (<age>, <number of friends with that age>) sorted in desc order by
    the number of friends and asc by the age.
    '''
    PARAMS = {'user_id': uid,
              'v': '5.52',
              'access_token': '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711'
              }
    now = datetime.now()
    friend_without_data = []

    req = f'https://api.vk.com/method/users.get'
    id = requests.get(req, params=PARAMS)

    if id.status_code != requests.codes.ok:
        raise Exception(f'{id.raise_for_status()}')

    id = id.json()
    if 'error' in id:
        raise Exception(f'{id["error"]["error_msg"]}')
    print(f'User: {id["response"][0]["first_name"]} {id["response"][0]["last_name"]}')

    PARAMS['fields'] = 'bdate'
    RESULT = {}

    req = f'https://api.vk.com/method/friends.get'
    years_friends = requests.get(req, params=PARAMS).json()

    for friend in years_friends['response']['items']:
        try:
            age_delta = relativedelta(now, datetime.strptime(friend['bdate'], '%d.%m.%Y')).years
            if age_delta not in RESULT:
                RESULT[age_delta] = 1
            else:
                RESULT[age_delta] = RESULT[age_delta] + 1
        except Exception as ex:
            friend_without_data.append(f'{friend["first_name"]} {friend["last_name"]}')

    RESULT = list(RESULT.items())
    RESULT.sort(key=lambda x: (-x[1], x[0]))
    print(f'***\nFriends without full bdata:\t{", ".join(friend_without_data)}')

    return RESULT


if __name__ == '__main__':
    UID = '1234567'  # '53886494'  # ''210700286'
    res = calc_age(UID)
    print(res)
