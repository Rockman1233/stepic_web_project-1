# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class QuestionManager(models.Manager):
	def new():
		pass
	def popular():
		pass

class Question(models.Model):
	objects = QuestionManager()
	title = models.CharField(default="", max_length=255)
	text = models.TextField(default="")
	added_at = models.DateField(null=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	likes = models.ManyToManyField(User,related_name="q_to_likes")
	
	def get_absolute_url(self):
		return reverse('question', kwargs={'pk': self.pk})

class Answer(models.Model):
	text = models.TextField(default="")
	added_at = models.DateField(null=True)
	question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
	author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
