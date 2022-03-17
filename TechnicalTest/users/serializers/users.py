"""Users Serializers"""
# Django
from django.contrib.auth import authenticate


# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token


# Models
from users.models import User


class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer"""
    class Meta:
        """Meta class"""
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        )


class UserAuthSerializer(serializers.Serializer):
    """User Auth serializer.
    Handle the authentication request data"""

    user = serializers.EmailField(default="")
    password = serializers.CharField(default="")

    def validate(self, data):
        """Check credentials and structure of request"""

        if data['user'] == "" or data['password'] == "" or len(self.initial_data) > 2:
            raise serializers.ValidationError(
                {"error_message": ("Petición inválida",)})

        user_authenticated = authenticate(
            username=data['user'], password=data['password'])
            
        if not user_authenticated:
            raise serializers.ValidationError(
                {"error_message": ("Credenciales inválidas o usuario inexistente",)})

        self.context['user'] = user_authenticated
        return data


    def create(self, data):
        """Generate or retrieve new token"""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key
