from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
            "avatar",
            "phone_number",
            "birthday",
            "half_money",
            "password",
        )
        read_only_fields = ("id", "avatar", "half_money", "birthday")
    
    def create(self, validated_data):
        password = validated_data.get("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user
