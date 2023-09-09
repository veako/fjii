import logging

import image
import share
import util

logging.getLogger().setLevel(logging.INFO)
if __name__ == '__main__':
    lines = share.article_list()
    for article in lines:
        try:
            if util.is_limit():
                # 分数上限
                break
            """
            url_type = article['urlType']
            分享类型
                0.抖音
                1.微信
                2.微博
                3.头条
                7.知乎
            """
            image.multi_upload(article)
            # 分享刷分
            share.share_method(article)
        except Exception as e:
            logging.error(e)