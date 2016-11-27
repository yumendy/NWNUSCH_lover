from django.contrib import admin
from statistics.models import Info


class InfoAdmin(admin.ModelAdmin):
    list_display = (
    'name', 'sex', 'birthday', 'grade', 'class_num', 'college', 'major', 'city', 'qq_num', 'wx_num', 'create_time')


admin.site.register(Info, InfoAdmin)
