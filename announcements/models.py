from django.db import models


class Announcement(models.Model):
    title = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    summary = models.TextField()
    content = models.TextField()
    publish_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-publish_date", "-created_date"]

    def __str__(self):
        return self.title
