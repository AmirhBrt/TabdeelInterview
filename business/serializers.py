from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from phonenumber_field.serializerfields import PhoneNumberField

from .models import Seller, ChargeRecord


class CreateSellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ['name', 'credit']

    def validate(self, data):
        name = data.get('name')
        all_names = Seller.objects.values_list('name', flat=True)
        if name in all_names:
            raise serializers.ValidationError(_('Seller has been created before'))
        return data

    def create(self, validated_data):
        seller = Seller.objects.create(**validated_data)
        ChargeRecord.objects.create(seller=seller, amount=seller.credit)
        return seller


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ['name', ]


class ChargeRecordSerializer(serializers.Serializer):
    seller = serializers.CharField(max_length=150, allow_null=False, allow_blank=False)
    customer = PhoneNumberField(max_length=150, allow_null=False, allow_blank=False)
    amount = serializers.IntegerField(allow_null=False)
    created_date = serializers.DateTimeField(allow_null=False, default=datetime.now)

    def validate(self, data):
        seller_name = data.get('seller')
        amount = data.get('amount')
        all_seller_name = Seller.objects.values_list('name', flat=True)
        if seller_name not in all_seller_name:
            raise serializers.ValidationError(_('No seller exists with this name'))
        seller = Seller.objects.get(name=seller_name)
        if seller.credit < amount:
            raise serializers.ValidationError(_('Seller has not enough balance'))
        return data

    def create(self, validated_data):
        customer_number = validated_data.get('customer')
        seller_name = validated_data.get('seller')
        amount = validated_data.get('amount')
        created_date = validated_data.get('created_date')
        seller = Seller.objects.get(name=seller_name)
        seller.credit -= amount
        seller.save()
        charge_record = ChargeRecord.objects.create(seller=seller, customer=customer_number,
                                                    amount=amount, created_date=created_date)
        return charge_record
