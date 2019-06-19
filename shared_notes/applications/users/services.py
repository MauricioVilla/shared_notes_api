# -*- encoding: utf-8 -*-
from shared_notes.applications.users import models


def consultUser(username):
    try:
        user = models.User.objects.filter(username=username).all()
        return user
    except Exception as e:
        print('Error al consultar usuario')
