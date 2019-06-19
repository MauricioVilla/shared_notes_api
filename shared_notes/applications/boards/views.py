# -*- encoding: utf-8 -*-

from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import mixins, views, viewsets

from shared_notes.applications.boards.models import Board, Idea
from shared_notes.applications.boards.serializers import BoardCreateSerializer, IdeaCreateSerializer


class BoardViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    """
    list: ViewSet for get all the boards of an user filtering by creator
    create: ViewSet for creation of boards associated with an user.
    retrieve: ViewSet for get boards by id
    update: ViewSet for update boards by id
    destroy: ViewSet for delete boards by id
    """
    permission_classes = (IsAuthenticated,)
    queryset = Board.objects.all()
    serializer_class = BoardCreateSerializer
    http_method_names = ['get', 'put', 'delete', 'post']
    filter_fields = ('created_by__id',)


class IdeaViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    """
    list: ViewSet for get all the ideas of an board filtering by id board
    create: ViewSet for creation of ideas associated with an board.
    retrieve: ViewSet for get ideas by id
    update: ViewSet for update ideas by id
    destroy: ViewSet for delete ideas by id
    """
    permission_classes = (IsAuthenticated,)
    queryset = Idea.objects.all()
    serializer_class = IdeaCreateSerializer
    lookup_field = 'board__id'
    filter_fields = ('created_by__id',)
    http_method_names = ['get', 'put', 'delete', 'post']


class GetIdeasBoard(views.APIView):
    """
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        title = request.GET.get('title')
        boards = self.get_boards(title)
        ideas = self.get_ideas()
        response = [boards, ideas]
        return Response(response)

    def get_boards(self, title):
        if title and title != 'undefined':
            boards = Board.objects.filter(title__contains=title).all()
        else:
            boards = Board.objects.all()
        if boards == None:
            return Response(status=404)
        boards_serializer = BoardCreateSerializer(boards, many=True)
        return boards_serializer.data

    def get_ideas(self):
        ideas = Idea.objects.all()
        ideas_serializer = IdeaCreateSerializer(ideas, many=True)
        return ideas_serializer.data


def approve_idea(request):
    """
    :param request:
    :return:Json
    """
    import json
    from django.http import HttpResponse
    default_content_type = 'application/json; charset=UTF-8'
    try:
        id = request.GET.get('id')
        if not id:
            raise Exception("id requerido...")
        idea = Idea.objects.get(id=id)
        idea.approved = 'SI'
        idea.save()
        return HttpResponse(json.dumps({
                             'success': True,
                             'result': idea
                         }), content_type=default_content_type)
    except Exception as e:
        return HttpResponse(json.dumps({
            'success': False,
            'errors': e.args
        }), content_type=default_content_type)
