from django.contrib import admin
from django.urls import path, include
from auth_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shopify/', include('shopify_auth.urls')),  # <--- Esta es la línea importante
    path('', views.home, name='home'),
]