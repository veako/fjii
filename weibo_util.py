import datetime
import io
import random

from PIL import Image, ImageDraw, ImageFont


def generate_like(fp='./image/weibo/like.png') -> bytes:
    """
    生成点赞图片
    ps:应该使用图片绘制，制造一张点赞的图片
    此处方法自行完善
    """
    image = Image.open(fp)
    draw = ImageDraw.Draw(image)

    random_point = (1, 1)  # 制造随机内容，修改文件md5值
    draw.text(random_point, "{}".format(str(random.random())))

    return image.tobytes()


def generate_comment(fp='./image/weibo/comment.png') -> bytes:
    """
    生成评论图片
    ps:应该使用图片绘制，制造一张评论的图片
    此处方法自行完善
    """
    image = Image.open(fp)
    # 创建一个可以在图片上绘图的对象
    draw = ImageDraw.Draw(image)

    random_point = (1, 1)  # 制造随机内容，修改文件md5值
    draw.text(random_point, "{}".format(str(random.random())))

    return image.tobytes()


def generate_forward(fp='./image/weibo/forward.png') -> bytes:
    """
    生成转发图片
    ps:应该使用图片绘制，制造一张转发的图片
    此处方法自行完善
    """
    image = Image.open(fp)
    # 创建一个可以在图片上绘图的对象
    draw = ImageDraw.Draw(image)

    random_point = (1, 1)  # 制造随机内容，修改文件md5值
    draw.text(random_point, "{}".format(str(random.random())))

    return image.tobytes()
