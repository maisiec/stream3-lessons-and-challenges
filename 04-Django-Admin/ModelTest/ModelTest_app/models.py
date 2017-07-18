# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Contact(models.Model):

	class Meta: # include this to ensure the build in IDE
		app_label = "ModelTest_app"

	first_name = models.CharField(max_length=225)
	last_name = models.CharField(max_length=225)
	mobile = models.CharField(max_length=20)

	def __str__(self):
		return ' '.join([
			self.first_name,
			self.last_name,
		])