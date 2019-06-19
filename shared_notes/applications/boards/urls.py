# -*- encoding: utf-8 -*-

from django.urls import path
from rest_framework import routers

from shared_notes.applications.boards.views import *

router = routers.SimpleRouter()
router.register(r'create', BoardCreateViewSet)
router.register(r'list', BoardListViewSet)
router.register(r'update', BoardUpdateViewSet)
router.register(r'delete', BoardDestroyViewSet)
router.register(r'ideas/create', IdeaCreateViewSet)
router.register(r'ideas/retrieve', IdeaRetrieveViewSet)
router.register(r'ideas/update', IdeaUpdateViewSet)
router.register(r'ideas/delete', BoardDestroyViewSet)

urlpatterns = [
    path('get_boards/', SearchBoard.as_view(), name='boards.get'),
    # path('ideas/approve/', approve_idea, name='ideas.approve')
] + router.urls