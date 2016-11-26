# coding=utf-8
from __future__ import unicode_literals

from django.db import models


class Info(models.Model):
    name = models.CharField(max_length=32)
    SEX_CHOICE = (
        ('M', u'男'),
        ('F', u'女'),
    )
    sex = models.CharField(max_length=1, choices=SEX_CHOICE)
    birthday = models.CharField(max_length=32)
    grade = models.IntegerField()
    class_num = models.IntegerField()
    teacher_name = models.CharField(max_length=32)
    college = models.CharField(max_length=128)
    major = models.CharField(max_length=32)
    city = models.CharField(max_length=128)
    qq_num = models.CharField(max_length=16, blank=True, null=True)
    wx_num = models.CharField(max_length=128, blank=True, null=True)
    can_long_distance_relationship = models.BooleanField(default=True)
    remarks = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name
