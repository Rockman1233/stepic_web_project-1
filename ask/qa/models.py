# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

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
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="q_author")
	likes = models.ManyToManyField(User, related_name="q_to_likes", blank=True)
	
	def get_url(self):
		return "/question/{}/".format(self.id)

class Answer(models.Model):
	text = models.TextField(default="")
	added_at = models.DateTimeField(auto_now_add=True)
	question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
	author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
