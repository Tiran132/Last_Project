"""Last_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from Last_Project.views import show_categories_page, show_main_page, show_one_category, show_site_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', show_categories_page),
    path('', show_main_page),
    path('categories/<int:category_id>', show_one_category),
    path('sites/<int:site_id>', show_site_page),
]
