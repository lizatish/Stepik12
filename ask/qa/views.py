from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import Http404
from .models import Question, Answer


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def new_questions(request):
    questions = Question.objects.new()
    page = request.GET.get('page', 1)
    limit = 10
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/question/'
    try:
        page = paginator.page(page)
    except EmptyPage:
        raise Http404
    except PageNotAnInteger:
        raise Http404
    context = {'paginator': paginator,
               'page': page
               }
    return render(request, 'questions_list.html', context)


def popular_questions(request):
    questions = Question.objects.popular()
    page = request.GET.get('page', 1)
    limit = 10
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/question/'
    try:
        page = paginator.page(page)
    except EmptyPage:
        raise Http404
    except PageNotAnInteger:
        raise Http404
    context = {'paginator': paginator,
               'page': page
               }
    return render(request, 'questions_list.html', context)


def question(request, id):
    try:
        id = int(id)
    except ValueError:
        raise Http404
    try:
        question = Question.objects.get(id=id)
    except Question.DoesNotExist:
        raise Http404
    context = {'question': question,
               'answers': question.answer_set.all()
               }
    return render(request, 'one_question.html', context)
