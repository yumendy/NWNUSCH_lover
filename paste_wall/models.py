from __future__ import unicode_literals

from django.db import models


class Paste(models.Model):
    name = models.CharField(max_length=64)
    grade = models.IntegerField(blank=True, null=True)
    class_num = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    author = models.CharField(max_length=64, blank=True, null=True)
    is_anonymous = models.BooleanField(default=True)
    is_checked = models.BooleanField(default=False)
    author_ip = models.GenericIPAddressField(blank=True, null=True)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.content

    class Meta:
        ordering = ['-create_time']
