from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from models import Seller


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'

    def validate(self, data):
        name = data.get('name', '')
        all_names = Seller.objects.values_list('name', flat=True)
        if name in all_names:
            raise serializers.ValidationError(_('Seller has been created before'))
        return data

    def create(self, validated_data):
        seller = Seller.objects.create(**validated_data)
        return seller

