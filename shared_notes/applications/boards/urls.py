# -*- encoding: utf-8 -*-

from django.urls import path
from rest_framework import routers

from shared_notes.applications.boards.views import *

router = routers.SimpleRouter()
router.register(r'create', BoardCreateViewSet)
router.register(r'update', BoardUpdateViewSet)
router.register(r'delete', BoardDestroyViewSet)
router.register(r'ideas/create', IdeaCreateViewSet)
router.register(r'ideas/retrieve', IdeaRetrieveViewSet)
router.register(r'ideas/list', IdeaListViewSet)
router.register(r'ideas/update', IdeaUpdateViewSet)
router.register(r'ideas/delete', BoardDestroyViewSet)

urlpatterns = [
    path('search', SearchBoardsAPIView.as_view(), name='boards.get'),
    path('list', BoardListAPIView.as_view(), name='boards.list')
] + router.urls