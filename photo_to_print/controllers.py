from .models import *
import wagtail.images as images


def list_pics():
    pic_list = images.models.Image.objects.all()
    # print(pic_list)
    return pic_list


def exchange_coupon(photo_id, coupon_code):
    pass