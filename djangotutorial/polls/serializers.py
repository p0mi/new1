from rest_framework import serializers
from .models import User  # Предполагаю, что у вас есть модель User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'