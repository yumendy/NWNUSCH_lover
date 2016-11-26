from django.contrib import admin
from paste_wall.models import Paste


class PasteAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade', 'class_num', 'email', 'author', 'is_checked', 'create_time')

admin.site.register(Paste, PasteAdmin)
