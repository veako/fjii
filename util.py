import requests

import config


def is_limit(api='api/userIntegralExceedLimitRemind/isTips'):
    """
    是否达到每天上限（一个有问题的接口，查询结果经常不准确）
    """
    url = config.global_url + api
    headers = {
        'Host': 'mt.fjii.com',
        'User-Agent': config.global_ua,
        'token': config.global_token,
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': 'token={}'.format(config.global_token)
    }
    response = requests.post(url, headers=headers)
    result = response.json()
    return False if result['data'] == 1 else True
