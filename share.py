# 处理数据，提取id
import json
import logging
import time

import jsonlines
import requests

import config

logging.getLogger().setLevel(logging.INFO)


def article_list(file_path='./data/article.jsonl'):
    file = open(file_path, "r+")
    return jsonlines.Reader(file)


# 分享获取积分
def share_method(article, api='api/wechatShareTask/shareSum'):
    if article['isType'] == 1:
        '''
        该类型分享需要数据解密（未完成逆向）
        '''
        return
    url = config.global_url + api
    payload = json.dumps({'wechat_share_task_id': article['id'], 'type': 1})
    headers = {
        'Host': 'mt.fjii.com',
        'User-Agent': config.global_ua,
        'token': config.global_token,
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': 'token={}'.format(config.global_token)
    }
    response = requests.post(url, headers=headers, data=payload)
    result = response.json()
    if result['message'] == '频繁分享，请稍后再试':
        print('分享频繁，程序休眠5min')
        time.sleep(5 * 60)
    logging.info("{}:{}".format(article['title'], result['message']))
    time.sleep(15)
