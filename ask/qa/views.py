# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse
from qa.models import Question
from qa.forms import AskForm, AnswerForm

# Create your views here.

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def paginate(request, qs):
	try:
		limit = int(request.GET.get('limit', 10))
	except ValueError:
		limit = 10
	if limit > 100:
		limit = 10
	try:
		page = int(request.GET.get('page', 1))
	except ValueError:
		raise Http404
	paginator = Paginator(qs, limit)
	try:
		page = paginator.page(page)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)
	return page, paginator

def mainpg(request):
	qs = Question.objects.order_by('-id')
	page, paginator = paginate(request, qs)
	paginator.baseurl = reverse('mainpg')
	return render(request, 'main.html', {
		'questions': page.object_list,
		'page': page,
		'paginator': paginator,
	})

def popular(request):
	qs = Question.objects.order_by('-rating')
	page, paginator = paginate(request, qs)
	paginator.baseurl = reverse('popular') + '?page='
	return render(request, 'popular.html', {
		'questions': page.object_list,
		'page': page,
		'paginator': paginator,
	})

def question(request, pk):
	question = get_object_or_404(Question, id=pk)
	answers = question.answer_set.all()
	return render(request, 'question.html', {
		'question': question,
		'answers': answers,
	})

def question_ask(request):
	if request.method == 'POST':
		form = AskForm(request.POST)
		if forms.is_valid():
			form._user = request.user
			ask = form.save()
			url = reverse('question', args=[ask.id])
			return HttpResponseRedirect(url)
	else:
		form = AskForm()
	return render(request, 'ask.html', {
		'form': form
	})

def question_ans(request)
	if request.method == 'POST':
		form = AnswerForm(request.POST)
		if from.is_valid():
			form._user = request.user
			answer = form.save()
			url = reverse('question', args=[answer.question.id])
			return HttpResponseRedirect(url)
	return HttpResponseRedirect('/')
