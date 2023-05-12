from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import re


def is_sanitized1(input_string):
    pattern = r"(\b(ALTER|CREATE|DELETE|DROP|EXEC(UTE){0,1}|INSERT( +INTO){0,1}|SELECT|UNION( +ALL){0,1}|UPDATE)\b|\-\-|\#)"

    if re.search(pattern, input_string, re.IGNORECASE):
        return False

    return True


def is_sanitized(request):
    if request.method == 'GET':
         return
         HttpResponse("Welcome to Naveen")

    elif request.method == "POST":
        input_string = request.POST.get('input')

        if is_sanitized1(input_string):
            result = {'result': 'sanitized'}
        else:
            result = {'result': 'unsanitized'}

        return JsonResponse(result)


def index(request):
    return HttpResponse("hello world");