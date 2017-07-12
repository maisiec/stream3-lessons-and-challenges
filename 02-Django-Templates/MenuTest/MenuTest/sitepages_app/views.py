# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.


def home(request):
	now = datetime.datetime.now()
	return render(request, "sitepages/home.html", {"current_date": now})

def contact(request):
	return render(request, "sitepages/contact.html")

def about(request):
	return render(request, "sitepages/about.html")
		