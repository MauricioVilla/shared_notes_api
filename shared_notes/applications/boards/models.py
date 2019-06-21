import uuid

from django.db import models
from shared_notes.applications.users.models import User


PUBLIC_PRIVATE_CHOICES = (
    ('Privado', 'Privado'),
    ('Publico', 'Publico'),
)

YES_NO_CHOICES = (
    ('Si', 'Si'),
    ('No', 'No'),
)


class TimeStampedModel(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)

    class Meta:
        abstract = True


class Board(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    type = models.CharField(choices=PUBLIC_PRIVATE_CHOICES, max_length=30, null=False, blank=False)
    author = models.CharField(max_length=500, null=False, blank=False)
    created_by = models.ForeignKey(User, null=False, blank=False, related_name='board_created_by', on_delete=models.PROTECT)
    updated_by = models.ForeignKey(User, null=True, blank=True, related_name='board_updated_by', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Tablero'
        verbose_name_plural = 'Tableros'
        ordering = ["-creation_date"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.author = self.created_by.nickname
        return super(Board, self).save(*args, **kwargs)


class Idea(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    board = models.ForeignKey(Board, null=False, blank=False, on_delete=models.CASCADE, related_name='ideas')
    description = models.TextField(max_length=500, null=False, blank=False, )
    approved = models.CharField(choices=YES_NO_CHOICES, null=False, blank=False, max_length=10)
    author = models.CharField(max_length=500, null=False, blank=False)
    created_by = models.ForeignKey(User, null=True, blank=False, related_name='idea_created_by', on_delete=models.PROTECT)
    updated_by = models.ForeignKey(User, null=True, blank=True, related_name='idea_updated_by', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Idea'
        verbose_name_plural = 'Ideas'
        ordering = ["-creation_date"]

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        self.author = self.created_by.nickname
        return super(Idea, self).save(*args, **kwargs)
