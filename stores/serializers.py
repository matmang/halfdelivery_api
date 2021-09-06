from rest_framework import serializers
from .models import Stores

# ? Model Serializer는 자동으로 create 와 update 함수를 만들어준다!
class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stores
        fields = [
            "id",
            "category",
            "store",
            "menu",
            "price",
            "minPrice",
            "delivTip",
            "expDelivTime",
            "openingHours",
        ]
