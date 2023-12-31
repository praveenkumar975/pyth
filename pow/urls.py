"""
URL configuration for pow project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
"""
from django.contrib import admin
from django.urls import path
from powcase import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/p0/dev_pow/',views.dev_pow),
    path('api/p0/waterpow/',views.water_pow),
    path('api/p0/fairpow/',views.fair_pow),
    path('api/po/stonespow/',views.stone_pow),
    path('api/p0/addbook/',views.addbook),
    path('api/p0/createbook/',views.create_book),
    path('api/p0/newbook/',views.new_book),
]
