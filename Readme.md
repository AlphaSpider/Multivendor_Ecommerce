Documentation

1. Create virtual environment env
2. Install Django
3. django-admin startproject backend_api
4. Install PostgreSQL
5. Install PgAdmin4
6. Install psycopg2-binary
4. install djangorestframewok
5. Import Django inbuilt User model to models.py by "from django.contrib.auth.models import User"

-------------Video-3-----------
6. Update urls patterns in urls.py(/backend_api) by including the created app's url:
    urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('main.urls'))
]
7. Create urls.py in the app (/main)
8. Inside the urls.py, import path(just like in the predefined urls.py) and views:
    from django.urls import path
    from .import views
    urlpatterns = [
        path('vendors/', views.VendorList.as_view()),
    ]

-------------Video-4-----------
9. Add authentication path in the urls.py and include "rest_framework.urls":
        path('api-auth/', include('rest_framework.urls')),


10. Authentication:
    in views.py import permission and specify the permission class = permissions.IsAuthenticated in class Vendorlist
    class VendorList(generics.ListAPIView):
    queryset=models.Vendor.objects.all()
    serializer_class=serializers.VendorSerializer
    permission_classes=[permissions.IsAuthenticated]
#only shows the data once the user logs in. This is the view level permission

11. Documentation for the Permission: https://www.django-rest-framework.org/api-guide/permissions/   
        Setting the permission Project level:
        a) create view for vendordetail, set path in url.py(main) >>>> path('vendor/<int:pk>', views.VendorDetail.as_view()),
            
            views.py:
            class VendorDetail(generics.RetrieveAPIView):
                queryset=models.Vendor.objects.all()
                serializer_class=serializers.VendorDetailSerializer
        b) Add Restframework Permissions in settings.py
            REST_FRAMEWORK = {
                'DEFAULT_PERMISSION_CLASSES': [
                'rest_framework.permissions.IsAuthenticated',
                ]
            }

12. Set the depth attribute of the Meta class to 1 (serializers.py):
            def __init__(self, *args, **kwargs):
                super(VendorSerializer, self).__init__(*args, **kwargs)
                self.Meta.depth = 1

13. In views.py, change the ListAPIView to ListCreateAPIView and RetriveAPIView to RetriveUpdateDestroyAPIView

-------------Video-5-----------

14. Register Product class in admin.

15. Add category to Product class as a foreignkey from ProductCategory and set on_delete to SET_NULL:
        category=models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True)
    Add vendor to the Product class as a foreignkey from Vendor just like above:
        vendor=models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)

16. Register ProductCategory class in admin.

17. Create ProductListSerializer just like other serializers.

18. Create ProductList view and connect it to the ProductListSerializer:
19. Set path for product listing in urls.py

20. Create ProductDetailSerializer just like other serializers.
21. Create ProductDetail view and connect it to the ProductDetailSerializer:
22. Set path for product detail in urls.py



23. -------------Video-6-----------
            JWT Authentication:

24. Install djangorestframework-simplejwt
25. In project level urls.py add
    from rest_framework_simplejwt import views as jwt_views and include the 2 url patterns for access and refresh tokens
    urlpatterns = [
    ...
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ...
]
    https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#installation

    JWT token gen req http://127.0.0.1:8000/api/token/
    {
        "username":"admin",
        "password":"1234"
    }


26. Add Authentication class inside restframework in settings.py
    REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

27. Generate Tokens:
    Install httpie or postman... then run this command in the terminal:
    http post http://127.0.0.1:8000/api/token/ username= password=
    *   Note down the two tokens access and refresh
    Requesting--------
    *   http http://127.0.0.1:8000/api/vendors/ "Authorization: Bearer #your access token"
    *   http http://127.0.0.1:8000/api/token/refresh/ refresh=         #your refresh token

28. -------------Video-7-----------

    Created Customer, Order and Order Items models
    Order Item for specific order since you can order multiple items in a single order