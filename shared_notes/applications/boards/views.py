# -*- encoding: utf-8 -*-
from django.db.models import Q

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics, mixins, views, viewsets

from shared_notes.applications.boards.models import Board, Idea
from shared_notes.applications.boards.serializers import *


### Boards
class BoardCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    create: ViewSet for creation of boards associated with an user.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Board.objects.all()
    serializer_class = BoardCreateSerializer
    http_method_names = ['post']


class BoardListAPIView(generics.ListAPIView):
    serializer_class = BoardReadSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Board.objects.all()
        author = self.request.query_params.get('author', None)
        if author is not None:
            queryset = queryset.filter(author=author)
        return queryset


class BoardUpdateViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    update: ViewSet for update boards by id
    """
    permission_classes = (IsAuthenticated,)
    queryset = Board.objects.all()
    serializer_class = BoardCreateSerializer
    http_method_names = ['put']


class BoardDestroyViewSet(mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    destroy: ViewSet for delete boards by id
    """
    permission_classes = (IsAuthenticated,)
    queryset = Board.objects.all()
    serializer_class = BoardCreateSerializer


class SearchBoardsAPIView(generics.ListAPIView):
    serializer_class = BoardReadSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Board.objects.all()
        params = self.request.query_params.get('params', None)
        if params is not None:
            queryset = queryset.filter(Q(author__icontains=params) | Q(title__icontains=params))
        return queryset


### Ideas

class IdeaCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    """
    permission_classes = (IsAuthenticated,)
    queryset = Idea.objects.all()
    serializer_class = IdeaCreateSerializer


class IdeaRetrieveViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    """
    permission_classes = (IsAuthenticated,)
    queryset = Idea.objects.all()
    serializer_class = IdeaReadSerializer


class IdeaListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    """
    permission_classes = (IsAuthenticated,)
    queryset = Idea.objects.all()
    serializer_class = IdeaReadSerializer


class IdeaUpdateViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    """
    permission_classes = (IsAuthenticated,)
    queryset = Idea.objects.all()
    serializer_class = IdeaCreateSerializer
    http_method_names = ['put']


class IdeaDestroyViewSet(mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    """
    permission_classes = (IsAuthenticated,)
    queryset = Idea.objects.all()
    serializer_class = IdeaCreateSerializer
