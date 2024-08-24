"""
URL configuration for AnyVICP2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from AnyVICP2 import pages

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pages.index),
    path('index/', pages.index),
    path('join/', pages.join),
    path('api/join/', pages.joinapi),
    path('result/', pages.result),
    path('admin/login/', pages.admin_login),
    path('api/admin_login/', pages.api_adminLogin),
    path('wadmin/index/', pages.admin_index),
    path('wadmin/websitemanage/', pages.admin_website),
    path('wadmin/anmentmnge/', pages.admin_announcementcreate),
    path('wadmin/api/changewebsite/', pages.admin_websiteeditpost),
    path('wadmin/webedit', pages.admin_websiteedit),
    path('wadmin/api/announcement_creation', pages.admin_announcement_createapi)
]
