from django.contrib import admin

from shared_notes.applications.boards.models import Board


class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'type')
    search_fields = ('title', 'type')
    fieldsets = (
        (('',), {
            'fields': (
                'id', 'title', 'description', 'type')
        }),
    )
    readonly_fields = ('created_by', 'updated_by', 'id')
    actions = None

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        if change:
            obj.updated_by = request.user
        super(BoardAdmin, self).save_model(request, obj, form, change)


admin.site.register(Board, BoardAdmin)
