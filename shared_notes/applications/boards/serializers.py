from rest_framework import serializers

from .models import Board, Idea


class BoardCreateSerializer(serializers.ModelSerializer):
    """
    """
    ideas = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Board
        fields = ('id', 'title', 'description', 'type', 'ideas', 'created_by')


class IdeaCreateSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Idea
        fields = ('id', 'board', 'description', 'approved', 'created_by')
