import uuid
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser
from django.db import models


@python_2_unicode_compatible
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nickname = models.CharField(max_length=120, null=True, blank=True)
    num_document = models.CharField(max_length=120, null=True, blank=True)
    created_by = models.ForeignKey('self', null=True, related_name="user_created_by", on_delete=models.PROTECT)
    updated_by = models.ForeignKey('self', null=True, related_name="user_updated_by", on_delete=models.PROTECT)

    def __str__(self):
        return self.username if self.username else self.email

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'usuarios'

    def save(self, *args, **kwargs):
        self.nickname = self.username
        return super(User, self).save(*args, **kwargs)
