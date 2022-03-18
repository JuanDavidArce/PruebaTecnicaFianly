from rest_framework import authentication,exceptions

class BearerAuthentication(authentication.TokenAuthentication):
    keyword = 'Bearer'
    
    def authenticate_credentials(self, key):
        try:
            response = authentication.TokenAuthentication.authenticate_credentials(self,key)
        except exceptions.AuthenticationFailed:
            raise exceptions.AuthenticationFailed({"error_message":"token de acceso inválido"})
    
        return response