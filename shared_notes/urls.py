# -*- encoding: utf-8 -*-
"""shared_notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework_swagger.views import get_swagger_view

from shared_notes import settings

router = DefaultRouter()
schema_view = get_swagger_view(title='Shared Notes API')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view),
    path('api/v1/', include(router.urls)),
    path('api/v1/users/', include('shared_notes.applications.users.urls')),
    path('api/v1/boards/', include('shared_notes.applications.boards.urls')),
    path('api/v1/tokens/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/tokens/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/tokens/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
