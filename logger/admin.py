from django.contrib import admin

from logger.models import LogModel


@admin.register(LogModel)
class LogModelAdmin(admin.ModelAdmin):
    pass
