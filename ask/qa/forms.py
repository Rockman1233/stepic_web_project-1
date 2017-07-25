from django import forms
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from qa.models import Question, Answer

class AskForm(forms.Form):
	title = forms.CharField(max_length=255)
	text = forms.CharField(widget=forms.Textarea)
	title = forms.CharField(max_length=100)
	text = forms.CharField(widget=forms.Textarea)
	def clean(self):
		pass
	def save(self):
		ask = Question(**self.cleaned_data)
		ask.author_id = self._user.id
		ask.save()
		return ask

class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	question = forms.IntegerField(widget=forms.HiddenInput)
	def clean_question(self):
		question_id = self.cleaned_data['question']
		try:
			question = Question.objects.get(id=question_id)
		except Question.DoesNotExist:
		question = None
		return question

    def clean(self):
        pass

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.author_id = self._user.id
        answer.save()
        return answer
