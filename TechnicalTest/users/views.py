"""users views"""


# Django REST Framework
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action

# Permissions
from rest_framework.permissions import AllowAny

# Serializers
from .serializers import UserAuthSerializer,UserModelSerializer

# Models
from users.models import User


class UserViewSet(viewsets.GenericViewSet):
    """User view set.
    Handle auth and user information
    """
    queryset = User.objects.all()
    permissions =[AllowAny]

    
    @action(detail=False,methods=['post'])
    def auth(self,request):
        """User Auth"""
        serializer = UserAuthSerializer(data = request.data)
        if serializer.is_valid():
            user,token = serializer.save()
        else:
            error_response = {"error_message":serializer.errors["error_message"][0]}
            if error_response["error_message"] == "Petición inválida":
                return Response(error_response,status=status.HTTP_400_BAD_REQUEST)
            return Response(error_response,status=status.HTTP_401_UNAUTHORIZED)
            

        data = {
            'token':token,
            'user_name':UserModelSerializer(user).data["first_name"]
        }
        return Response(data,status = status.HTTP_200_OK)

