from rest_framework import serializers

from .models import Board, Idea


class BoardCreateSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Board
        fields = ('id', 'title', 'description', 'type', 'created_by')


class IdeaCreateSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Idea
        fields = ('id', 'board', 'description', 'approved', 'created_by')
