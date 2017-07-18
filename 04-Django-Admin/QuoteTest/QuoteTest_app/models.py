# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Quote(models.Model):
	"""docstring for Quote"""

	class Meta: # include this to ensure the build in IDE
		app_label = "QuoteTest_app" 

	author_first_name = models.CharField(max_length=225)
	author_last_name = models.CharField(max_length=225)
	quote = models.CharField(max_length=1000)
	
	def __str__(self):
		return ' '.join([
			self.author_first_name,
			self.author_last_name,
			self.quote
		])