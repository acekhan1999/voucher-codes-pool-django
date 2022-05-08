from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class SpecialOffer(models.Model):
    name =  models.CharField(max_length=30)
    discount = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class VoucherCode(models.Model):
    voucher =  models.CharField(max_length=8)
    special_offer = models.ForeignKey(SpecialOffer, on_delete=models.CASCADE, related_name="special_offer")
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    expiration_date = models.DateTimeField(null=False)
    used = models.BooleanField(default=False)
    date_used = models.DateTimeField(null=True, blank=True)

    def __str__(self):  
        return str(self.voucher) + " | " + str(self.special_offer)
    