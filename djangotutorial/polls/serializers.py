from rest_framework import serializers
from .models import User, Virtuals  # Предполагаю, что у вас есть модель User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Virtuals
        fields = ["id", "hostname", "protocol", "user_id", "address", "port", "user_vm", "password_vm", "ignore_cert"]