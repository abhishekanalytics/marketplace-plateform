from django.db import models
from Tradecore.models import CustomUser,Product


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True)
    quantity = models.IntegerField(default=1)
