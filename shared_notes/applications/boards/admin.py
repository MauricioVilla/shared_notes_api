from django.contrib import admin

from shared_notes.applications.boards.models import Board, Idea


class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'type', 'author', 'created_by', 'updated_by')
    search_fields = ('title', 'type')
    fieldsets = (
        (('',), {
            'fields': (
                'title', 'description', 'type', 'author')
        }),
    )
    readonly_fields = ('created_by', 'updated_by')
    actions = None

    def save_model(self, request, obj, form, change):
        if change:
            obj.updated_by = request.user
        else:
            obj.created_by = request.user
        super(BoardAdmin, self).save_model(request, obj, form, change)


class IdeaAdmin(admin.ModelAdmin):
    list_display = ('board', 'description', 'approved', 'author', 'created_by', 'updated_by')
    search_fields = ('board',)
    fieldsets = (
        (('',), {
            'fields': (
                'board', 'description', 'approved', 'author')
        }),
    )
    readonly_fields = ('created_by', 'updated_by')
    actions = None

    def save_model(self, request, obj, form, change):
        #
        if change:
            obj.updated_by = request.user
        else:
            obj.created_by = request.user
        super(IdeaAdmin, self).save_model(request, obj, form, change)


admin.site.register(Board, BoardAdmin)
admin.site.register(Idea, IdeaAdmin)
