from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "date_joined")

class IssueAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "executor", "date_created", "date_closed")

class ChatAdmin(admin.ModelAdmin):
    list_display = ("id", "commenter", "issue", "date")

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Chat, ChatAdmin)