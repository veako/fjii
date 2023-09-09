import json
import logging
import jsonlines

import requests

import config

logging.getLogger().setLevel(logging.INFO)


def save_article(data, file_path='./data/article.jsonl'):
    with jsonlines.open(file_path, 'a') as writer:
        for item in data['data']['list']:
            writer.write(item)


# 保存文章到本地
def search_article(api='api/wechatShareTask/list', page=1):
    result = object
    logging.info('抓取第：{} 页文章'.format(page))
    url = config.global_url + api
    payload = 'serviceId=1&secondaryColumn=&pageSize=10&pageNo={}'.format(page)
    headers = {
        'Host': 'mt.fjii.com',
        'User-Agent': config.global_ua[0],
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    try:
        response = requests.post(url, headers=headers, data=payload)
        result = response.json()
        save_article(result)
        page += 1
    except Exception as e:
        logging.error(e)
    if page < result['data']['pages']:
        search_article(page=page)


if __name__ == '__main__':
    search_article()
