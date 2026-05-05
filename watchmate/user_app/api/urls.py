from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from user_app.api.views import  register_user,logout_user,register_user_with_jwt

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('login/', obtain_auth_token ,name='login'),
    
    
    path('register/', register_user,name='register'),
    path('register_with_jwt/', register_user_with_jwt,name='register_jwt'),
    
    
    
    path('logout/', logout_user,name='logout'),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
ou