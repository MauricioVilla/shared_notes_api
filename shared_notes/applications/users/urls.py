# -*- encoding: utf-8 -*-
from django.urls import path
from rest_framework import routers

from shared_notes.applications.users import views

router = routers.SimpleRouter()
router.register(r'', views.UserViewSet)
router.register(r'', views.UserCreateViewSet)
router.register(r'get_user', views.GetUserByUsernameViewSet)

urlpatterns = [
    # path('', views.GetUserByUsernameApiView.as_view(), name='user.get'),
] + router.urls
