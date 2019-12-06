from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from .models import Question, Theme
from .scrapper import get_questions_from_website
import json


def json_theme(rq):
    if rq.GET.get('id'):
        t = get_object_or_404(Theme, pk=rq.GET['id'])
        return HttpResponse(serializers.serialize("json", [t, ]))
    else:
        return HttpResponse(serializers.serialize("json", Theme.objects.all()))


def json_question(rq):
    if rq.GET.get('id'):
        q = get_object_or_404(Question, pk=rq.GET['id'])
        return HttpResponse(serializers.serialize("json", [q, ]))
    elif rq.GET.get('theme'):
        t = get_object_or_404(Theme, pk=rq.GET.get('theme'))
        return HttpResponse(serializers.serialize("json", [t, ]))
    else:
        return HttpResponse(serializers.serialize("json", Question.objects.all()))


def update_questions(rq):
    questions = get_questions_from_website()
    for t in questions:
        nom_theme = t["theme"]
        try:
            theme = Theme.objects.get(nom__iexact=nom_theme)
        except:
            theme = Theme(nom=nom_theme).save()
            theme = Theme.objects.get(nom__iexact=nom_theme)
        finally:
            theme.question_set.create(question=t["question"], corps=t["corps"])
    return HttpResponse("Updated")