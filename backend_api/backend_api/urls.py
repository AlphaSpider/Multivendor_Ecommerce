"""
URL configuration for backend_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))


    http post http://127.0.0.1:8000/api/token/ username=admin password=1234

{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc2MTc1MTg5NCwiaWF0IjoxNzYxNjY1NDk0LCJqdGkiOiIzZWIyNzlkNGI5MWQ0MDc1OTY0Y2ExODk2ZWVkMWE0NiIsInVzZXJfaWQiOiIxIn0.CyWpl1sSKCi30p-9sqKAaeixSZn4gWRzGp4kgO4Z9Lg",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzYxNjY1Nzk0LCJpYXQiOjE3NjE2NjU0OTQsImp0aSI6ImYxYmE1YzRhNTBhZTQ2MzQ5YjVmYmJkZDc1ODEzNzQyIiwidXNlcl9pZCI6IjEifQ._wuk2aRZCKbLkekZNOqsvwxNIv2hxb9XCE1mFZzQr3I"
}

    http http://127.0.0.1:8000/api/vendors/ "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU1NTA5Mjc5LCJpYXQiOjE3NTU1MDg5NzksImp0aSI6IjA4MjRiNWIwOTIzMzQxMjg5MDM2NjQ4ZDc0NzBjZGU5IiwidXNlcl9pZCI6IjEifQ.r_QEms0FRm5Aczf6vvQYv2nZSe1o-0k8lZ_XO0xb7Os"


    http http://127.0.0.1:8000/api/token/refresh/ refresh=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc2MTc1MTg5NCwiaWF0IjoxNzYxNjY1NDk0LCJqdGkiOiIzZWIyNzlkNGI5MWQ0MDc1OTY0Y2ExODk2ZWVkMWE0NiIsInVzZXJfaWQiOiIxIn0.CyWpl1sSKCi30p-9sqKAaeixSZn4gWRzGp4kgO4Z9Lg


"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('main.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls')),
]  
