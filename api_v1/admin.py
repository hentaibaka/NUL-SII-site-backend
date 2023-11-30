from django.contrib import admin, messages
from .models import *

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'brief_title', 'is_realized', 'type', 'slug']
    list_display_links = ['id']
    list_editable = ['is_realized']
    ordering = ['id', 'title']
    actions = ['set_realized', 'set_in_progress']
    search_fields = ['title']
    list_filter = ['is_realized']

    @admin.display(description='Название')
    def brief_title(self, project: Project):
        return project.title[:20] + '...' if len(project.title) > 20 else project.title
    
    @admin.action(description='Пометить как "реализовано"')
    def set_realized(self, request, queryset):
        count = queryset.update(is_realized=Project.StatusChoices.REALIZED)
        self.message_user(request, f'{count} проектов помечено как "реализовано"', messages.SUCCESS)

    @admin.action(description='Пометить как "в разработке"')
    def set_in_progress(self, request, queryset):
        count = queryset.update(is_realized=Project.StatusChoices.IN_PROGRESS)
        self.message_user(request, f'{count} проектов помечено как "в разработке"', messages.WARNING)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'last_name', 'first_name', 'patronymic', 'link']
    list_display_links = ['id']
    list_editable = ['link']
    ordering = ['id', 'last_name', 'first_name', 'patronymic']

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'brief_description', 'link']
    list_display_links = ['id']
    list_editable = ['link']
    ordering = ['id', 'title']
    search_fields = ['title', 'description']

    @admin.display(description='Описание')
    def brief_description(self, publication: Publication):
        return publication.title[:20] + '...' if len(publication.title) > 20 else publication.title

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_create', 'name', 'email', 'brief_question']
    list_display_links = ['id']
    ordering = ['date_create', 'id']
    search_fields = ['name', 'email', 'question']
    list_filter = ['date_create']

    @admin.display(description='Вопрос')
    def brief_question(self, contact: Contact):
        return contact.question[:20] + '...' if len(contact.question) > 20 else contact.question