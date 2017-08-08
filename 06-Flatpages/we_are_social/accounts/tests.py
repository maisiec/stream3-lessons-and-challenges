# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from views import profile
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response

# Create your tests here

class ProfilePageTest(TestCase):
	def test_profile_page_reseolves(self):
		profile_page = resolve ('/profile/')
		self.assertEqual(profile_page.func, profile)

	