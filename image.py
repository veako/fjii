import json
import logging

import requests

import config
import weibo_util


def multi_upload(article, path='api/wechatShareTaskCommon/multiUpload'):
    url = config.global_url + path
    task = task_info(article['id'])
    payload = multi_upload_body(task)
    headers = {
        'Host': 'mt.fjii.com',
        'User-Agent': config.global_ua,
        'token': config.global_token,
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': 'token={}'.format(config.global_token)
    }
    response = requests.post(url, headers=headers, data=payload)
    result = response.json()
    logging.info("{}:{}".format(article['title'], result['message']))


def image_binary(image_bytes) -> bytes:
    """
    将图片数据合成完整的上传数据
    """
    data = (
        b'--f32sax4a-50fe-4273-ab63-f36db4383471\r\n'
        b'Content-Disposition: form-data; name="file"; filename="Screenshot.jpg"\r\n'
        b'Content-Type: image/jpeg\r\n'
        b'\r\n'
    )
    data += image_bytes
    data += (
        b'\r\n'
        b'--f32sax4a-50fe-4273-ab63-f36db4383471\r\n'
        b'Content-Disposition: form-data; name="token_header"\r\n'
        b'Content-Type: text/plain; charset=utf-8\r\n'
        b'\r\n'
        b'\r\n'
        b'--f32sax4a-50fe-4273-ab63-f36db4383471\r\n'
        b'Content-Disposition: form-data; name="type"\r\n'
        b'Content-Type: text/plain; charset=utf-8\r\n'
        b'\r\n'
        b'img\r\n'
        b'--f32sax4a-50fe-4273-ab63-f36db4383471\r\n'
        b'Content-Disposition: form-data; name="formSource"\r\n'
        b'Content-Type: text/plain; charset=utf-8\r\n'
        b'\r\n'
        b'1\r\n'
        b'--f32sax4a-50fe-4273-ab63-f36db4383471--\r\n'
    )
    return data


def upload_image(image_bytes, api='api/wechatShareTaskCommon/uploadImgSupplement'):
    """
    上传图片
    """
    image_bytes = image_binary(image_bytes)
    url = config.global_url + api  # 替换为实际的API地址
    # 构建请求头部
    headers = {
        '''
        此处请求头的boundary理论上应该为随机的uuid，要修改请一并修改image_binary函数中的boundary字符串
        '''
        'Content-Type': 'multipart/form-data; boundary=f32sax4a-50fe-4273-ab63-f36db4383471',
    }
    data = image_binary(image_bytes)
    response = requests.post(url, headers=headers, data=data)
    return response.json()['data']


def task_info(task_id, api='api/wechatShareTaskCommon/queryTaskSupplyInfo'):
    """
    查询文章补录数据
    """
    payload = json.dumps({"wechatShareId": task_id})
    url = config.global_url + api
    headers = {
        'Host': 'mt.fjii.com',
        'User-Agent': config.global_ua,
        'token': config.global_token,
        'Content-Type': 'application/json;charset=UTF-8'
    }
    response = requests.post(url, headers=headers, data=payload)
    return response.json()['data']


def multi_upload_body(task_data):
    id = task_data['taskInfo']['id']
    url_type = task_data['taskInfo']['urlType']
    body = {'wechatShareId': id}

    '''
    点赞
    '''
    like_list = task_data['likeUploadedInfo']
    for i in range(len(like_list), task_data['likeLimitNum']):
        data = None
        if url_type == 1:
            # 此处自行仿照微博类型文章生成图片数据
            pass
        elif url_type == 2:
            # 此处自行仿照微博类型文章生成图片数据
            pass
        elif url_type == 3:
            data = weibo_util.generate_like()
        if data is not None:
            data = weibo_util.generate_like()
            fp = upload_image(data)['filePath']
            temp = {'path': fp, 'reducePath': fp, 'id': None}
            like_list.append(temp)
    body['likeImages'] = like_list

    '''
    评论
    '''
    comment_list = task_data['commentUploadedInfo']
    for i in range(len(comment_list), task_data['commentLimitNum']):
        data = None
        if url_type == 1:
            # 此处自行仿照微博类型文章生成图片数据
            pass
        elif url_type == 2:
            # 此处自行仿照微博类型文章生成图片数据
            pass
        elif url_type == 3:
            data = weibo_util.generate_comment()
        if data is not None:
            data = weibo_util.generate_comment()
            fp = upload_image(data)['filePath']
            temp = {'path': fp, 'reducePath': fp, 'id': None}
            comment_list.append(temp)
    body['commentImages'] = comment_list

    '''
    转发
    '''
    forward_list = task_data['forwardUploadedInfo']
    for i in range(len(forward_list), task_data['forwardLimitNum']):
        data = None
        if url_type == 1:
            # 此处自行仿照微博类型文章生成图片数据
            pass
        elif url_type == 2:
            # 此处自行仿照微博类型文章生成图片数据
            pass
        elif url_type == 3:
            data = weibo_util.generate_forward()
        if data is not None:
            fp = upload_image(data)['filePath']
            temp = {'path': fp, 'reducePath': fp, 'id': None}
            forward_list.append(temp)
    body['forwardImages'] = forward_list
    return json.dumps(body)
