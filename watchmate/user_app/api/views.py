from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework import generics
# from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from user_app.api.serializer import RegistrationSerializer

from rest_framework_simplejwt.tokens import RefreshToken





@api_view(['POST'])
def logout_user(request):
    if request.method == 'POST':
     request.user.auth_token.delete()
     return Response({'msg': 'Logged out successfully'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = RegistrationSerializer(data=request.data)
    
    if serializer.is_valid():
        account = serializer.save()  # Save the user
        
        # Create or get token
        token, created = Token.objects.get_or_create(user=account)

        #  Return success response with token
        return Response({
            'msg': 'User registered successfully',
            'username': account.username,
            'email': account.email,
            'token': token.key
        }, status=status.HTTP_201_CREATED)
    
    #  Return errors if validation fails
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
@permission_classes([AllowAny])
def register_user_with_jwt(request):
    serializer = RegistrationSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        account = serializer.save()  # Save the user
        
        # Create or get token

        refresh = RefreshToken.for_user(account)
        data['msg'] = 'User registered successfully'
        data['token'] = {
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }
        data['username']=account.username,
        data['email']= account.email        
        return Response(data, status=status.HTTP_201_CREATED)
    
    #  Return errors if validation fails
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





        
            