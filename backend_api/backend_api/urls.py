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
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1NjU3NTc3OSwiaWF0IjoxNzU2NDg5Mzc5LCJqdGkiOiI0ZDJjMDk2NGUyY2M0M2M3ODQxNTgxMWI2ZDQ4NzUyMiIsInVzZXJfaWQiOiIxIn0.z8hXEEgqLVH6CnNkWT5zkDx-ypd6mDUIh1rBNdKjTCE",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU2NDg5Njc5LCJpYXQiOjE3NTY0ODkzNzksImp0aSI6ImI2ZWNjNDg2OGEzYTQyZjhiNGE2ZTUxODEzYmQ1M2ZiIiwidXNlcl9pZCI6IjEifQ.9N0OX76VhBphd0sdXbnh54P6Hp0j11PNT4toJUPaoWQ"
}

    http http://127.0.0.1:8000/api/vendors/ "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU1NTA5Mjc5LCJpYXQiOjE3NTU1MDg5NzksImp0aSI6IjA4MjRiNWIwOTIzMzQxMjg5MDM2NjQ4ZDc0NzBjZGU5IiwidXNlcl9pZCI6IjEifQ.r_QEms0FRm5Aczf6vvQYv2nZSe1o-0k8lZ_XO0xb7Os"


    http http://127.0.0.1:8000/api/token/refresh/ refresh=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1NTU5NTM3OSwiaWF0IjoxNzU1NTA4OTc5LCJqdGkiOiIzNzE0ZDlkYzEyNDU0NTJkOGRhZTlhMjkyZDFiMzM3ZCIsInVzZXJfaWQiOiIxIn0.sE11XVUIi8zDrE8GTFwGQkWlGE8nr_YSfVKl_yi30Bg


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
