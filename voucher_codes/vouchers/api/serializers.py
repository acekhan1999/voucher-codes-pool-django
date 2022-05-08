from rest_framework import serializers

from vouchers.models import SpecialOffer, VoucherCode

class SpecialOfferSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = SpecialOffer
        fields = "__all__"


class VoucherSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='customer.email')
    
    class Meta:

        model = VoucherCode
        fields = ['id' ,'voucher', 'expiration_date', 'used', 'date_used','customer', 'email']
        # exclude = ['special_offer', 'customer']