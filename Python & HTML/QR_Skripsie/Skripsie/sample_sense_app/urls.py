"""Skripsie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views


app_name = "sample_sense_app"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.homepage, name="homepage"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),

    path("add_sample", views.add_sample, name="add_sample"),
    path("add_feed_sample", views.add_feed_sample, name="add_feed_sample"),
    path("add_residue_sample", views.add_residue_sample, name="add_residue_sample"),

    path("feed_samples", views.list_feed_samples, name="feed_samples"),
    path("view_feed_sample/<sample_id>", views.view_feed_sample, name="view_feed_sample"),
    path("update_feed_sample/<sample_id>", views.update_feed_sample, name="update_feed_sample"),

    path("residue_samples", views.list_residue_samples, name="residue_samples"),
    path("view_residue_sample/<sample_id>", views.view_residue_sample, name="view_residue_sample"),
    path("update_residue_sample/<sample_id>", views.update_residue_sample, name="update_residue_sample"),
] 
