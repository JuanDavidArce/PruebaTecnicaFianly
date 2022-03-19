"""users views"""


# Django REST Framework
from rest_framework import viewsets,status,exceptions
from rest_framework.response import Response
from rest_framework.decorators import action

# Permissions
from rest_framework.permissions import AllowAny,IsAuthenticated

# Serializers
from .serializers import UserAuthSerializer,UserModelSerializer

# Models
from users.models import User



class UserViewSet(viewsets.GenericViewSet):
    """User view set.
    Handle auth and user information
    """
    queryset = User.objects.all()

    def get_serializer_class(self):
        """Return serializer based on action."""
        if self.action == "auth":
            return UserAuthSerializer
    
    def get_permissions(self):
        """Assign permissions based on action"""
        if self.action == 'auth':
            permissions =[AllowAny()]
        else:
            permissions =[IsAuthenticated()]
        return permissions
    
    @action(detail=False,methods=['post'])
    def auth(self,request):
        """User Auth"""
        try:
            serializer = UserAuthSerializer(data = request.data)
        except exceptions.ParseError:
            error_response = {"error_message":"Petición inválida"}
            return Response(error_response,status=status.HTTP_400_BAD_REQUEST)
        
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

    @action(detail=False,methods=['get'])
    def user(self,request):
        """Users Information"""
        response = UserModelSerializer(self.queryset,many = True).data
        return Response(response,status = status.HTTP_200_OK)

