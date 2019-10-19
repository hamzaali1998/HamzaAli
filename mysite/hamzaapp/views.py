# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    a = 7

    if a >1:
        for i in range(2, a+1):
            if (a % i) == 0:
                b = "not a prime number" 
                break
            else:
                b = "its a prime number"
                break
    else:
        b = "not a prime number"

    return HttpResponse(str(a) + "<br>" + b)


