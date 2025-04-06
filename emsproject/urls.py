"""
URL configuration for emsproject project.

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
from emsapp import views
from emsapp.views import no_access

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin panel
    path('home/', views.homeview, name='home'),  # Ensure home is accessible at '/'
    path('hr/', views.hrview, name='hr_manager'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('view_employees/', views.view_employees, name='view_employees'),
    path('add_news/', views.add_news, name='add_news'),
    path('view_news/', views.view_news, name='view_news'),
    path('add_calendar/', views.add_calendar, name='add_calendar'),
    path('view_calendar/', views.view_calendar, name='view_calendar'),
    path('no-access/', views.no_access, name='no_access'),
    path('technical_issues/', views.technical_issues, name='technical_issues'),
]
