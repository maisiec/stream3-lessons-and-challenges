# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from views import profile
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from .models import User
# Create your tests here

class ProfilePageTest(TestCase):
	def test_profile_page_reseolves(self):
		profile_page = resolve ('/profile/')
		self.assertEqual(profile_page.func, profile)

class CustomUserTest(TestCase):
	
	def test_manager_create(self):
		user = User.objects._create_user(None, "test@test.com", "password", False, False)
		self.assertIsNotNone(user)

		with self.assertRaises(ValueError):
			user = User.objects._create_user(None, None, "password", False, False)
			
		