from django.contrib import admin

from .models import Announcement


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "department", "publish_date", "created_date")
    list_filter = ("department", "publish_date")
    search_fields = ("title", "summary", "content")
