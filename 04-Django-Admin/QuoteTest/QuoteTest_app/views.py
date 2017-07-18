# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from QuoteTest_app.models import Quote

# Create your views here.
def get_quotes(request):
	return render(request, "QuoteTest/home.html",
		{'quote_list': Quote.objects.all()})