# -*- encoding: utf-8 -*-

from django.urls import path
from rest_framework import routers

from shared_notes.applications.boards.views import *

router = routers.SimpleRouter()
router.register(r'', BoardViewSet)
router.register(r'idea', IdeaViewSet)
# router.register(r'ideas', IdeaModelViewSet)
# router.register(r'ideas/approve', IdeaModelViewSet)

urlpatterns = [
    # path('get_boards/', GetBoardIdeas.as_view(), name='boards.get'),
    # path('approve_idea/', approve_idea, name='ideas.approve')
] + router.urls