# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contribauth.models import User

# Create your models here.

class Question(models.Model):
	title = models.CharField(default="", max_lehgth=255)
	text = models.TextField(default="")
	added_at = models.DateField(null=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	likes = models.ManyToManyField(User,related_name="q_to_likes")

class Answer(models.Model):
	text = models.TestField(default="")
	added_at = models.DateField(null=True)
	question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
	author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
