# -*- coding:utf-8 -*-

from __future__ import unicode_literals
from django.db import models


KIND_CHOICES=(
        ('Python Tech','Python Tech'),
        ('DB Tech','DB Tech'),
        ('Finical','Finical'),
        ('Text','Text'),
        ('xinqing','xinqing'),
        ('other','other')
        )

class Moment(models.Model):
    content=models.CharField(max_length=200)
    user_name=models.CharField(max_length=20,default='None')
    kind=models.CharField(max_length=20,choices=KIND_CHOICES,default=KIND_CHOICES[0])

