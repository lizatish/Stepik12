from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import Http404
from .models import Question
from .forms import AnswerForm, AskForm


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


def show_question(request, id):
    try:
        id = int(id)
    except ValueError:
        raise Http404
    try:
        question = Question.objects.get(id=id)
    except Question.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        form = AnswerForm(initial={'question': question.id})
    else:
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/question/' + str(id) + '/')

    context = {'question': question,
               'answers': question.answer_set.all(),
               'form': form,
               'url': '/question/' + str(id) + '/'
               }
    return render(request, 'one_question.html', context)


def create_question(request):
    if request.method == 'GET':
        form = AskForm()
    else:
        form = AskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/question/' + str(len(Question.objects.all())) + '/')
    return render(request, 'create_question.html', {'form': form})
