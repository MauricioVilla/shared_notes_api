from rest_framework import serializers

from shared_notes.applications.users.serializers import UserSerializer
from .models import Board, Idea


class BoardReadSerializer(serializers.ModelSerializer):
    """
    """
    ideas = serializers.StringRelatedField(many=True, read_only=True)
    created_by = UserSerializer()

    class Meta:
        model = Board
        fields = ('id', 'title', 'description', 'type', 'author', 'ideas', 'created_by')


class BoardCreateSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = Board
        fields = ('id', 'title', 'description', 'type', 'created_by')


class IdeaReadSerializer(serializers.ModelSerializer):
    """
    """
    board = BoardCreateSerializer(read_only=True)
    # board_title = serializers.ReadOnlyField(source='board.title')

    class Meta:
        model = Idea
        fields = ('id', 'board', 'description', 'approved',  'created_by')  # 'board_title',


class IdeaCreateSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = Idea
        fields = ('id', 'board', 'description', 'approved',  'created_by')
