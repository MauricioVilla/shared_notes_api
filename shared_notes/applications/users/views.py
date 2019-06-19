# -*- encoding: utf-8 -*-

from rest_framework.response import Response
from rest_framework import mixins, status, views, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from shared_notes.applications.users import services
from shared_notes.applications.users.serializers import UserSerializer, CreateUserSerializer
from shared_notes.applications.users.models import User
from .permissions import IsUserOrReadOnly


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    """
    retrieve:
    ViewSet for get users by id

    update:
    ViewSet for update users by id

    destroy:
    ViewSet for delete users by id
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'put', 'delete']

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UserCreateViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    ViewSet for creation of users
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)


class GetUserByUsernameViewSet(mixins.RetrieveModelMixin,
                               viewsets.GenericViewSet):
    """
    ViewSet for get user by username
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'nickname'


class GetUserByUsernameApiView(views.APIView):
    """
    ApiView for consult user by username
    :return: Json
    """
    permission_classes = (IsAuthenticated,)

    def get_object(self, username):
        user = services.consultUser(username)
        if user:
            return user
        return False

    def get(self, request, format=None):
        username = request.GET.get('username')
        user = self.get_object(username)
        if user:
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
