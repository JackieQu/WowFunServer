from django.contrib import admin
from .models import Snippet

# Register your models here.
class SnippetAdmin(admin.ModelAdmin):
    list_display = ('pk', 'owner', 'title', 'code', 'language', 'created')

admin.site.register(Snippet, SnippetAdmin)