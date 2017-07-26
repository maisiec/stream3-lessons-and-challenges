# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render


class PaypalStoreConfig(AppConfig):
    name = 'paypal_store'

@csrf_exempt
def paypal_return(request):
	args = {'post': request.POST, 'get':request.GET}
	return render(request, 'paypal/paypal_return.html', args)


def paypal_cancel(request):
	args = {'post':request.POST, 'get':request.GET}
	return render(request, 'paypal/paypal_cancel.html', args)

