from django.db import models
from django.utils.translation import gettext as _


class Stores(models.Model):
    # ! 왜인지는 모르겠지만 이게 있어야 INSERT failed: datatype mismatch 오류가 안 뜸.
    id = models.IntegerField(primary_key=True)
    # _ 붙인 이유는 그냥 habit임. 나중에 translation 하게되면 유용함.
    category = models.CharField(_("category"), max_length=255)
    store = models.CharField(_("store"), max_length=255)
    menu = models.CharField(_("menu"), max_length=255)
    price = models.CharField(_("price"), max_length=255)  # ? DB 수정 필요
    minprice = models.CharField(_("minprice"), max_length=255)  # ? DB 수정 필요
    delivTip = models.CharField(_("delivTip"), max_length=255)  # ? DB 수정 필요
    expDelivTime = models.CharField(_("expDelivTime"), max_length=255)
    openingHours = models.CharField(_("openingHours"), max_length=255)
