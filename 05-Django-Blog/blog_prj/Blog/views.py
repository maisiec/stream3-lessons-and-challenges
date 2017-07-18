# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
	"""
	Create a view that will return a
	list of Posts that were published prior to 'now'
	and render them to the 'blogpost.html' template
	"""
	posts = Post.objects.filter(published_date_lte=timezone.now()
		).order_by('-published_date')
	return render(request, "blogposts.html", {'posts':posts})
	