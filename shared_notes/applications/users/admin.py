import datetime

from django.contrib import admin

from shared_notes.applications.users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'num_document')
    search_fields = ('username', 'password', 'first_name', 'last_name', 'email', 'num_document')
    fieldsets = (
        (('',), {
            'fields': (
                'id', 'nickname', 'username', 'password', 'first_name', 'last_name', 'email', 'num_document', )
        }),
    )
    readonly_fields = ('created_by', 'updated_by', 'id')
    actions = None

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        if change:
            obj.updated_by = request.user
        super(UserAdmin, self).save_model(request, obj, form, change)


admin.site.register(User, UserAdmin)
