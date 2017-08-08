# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from home.views import get_index
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response

# Create your tests here.
class SimpleTest(TestCase):
	def test_adding_something_simple(self):
		self.assertEqual( 1 + 2, 3 )

	def test_adding_something_isnt_equal(self):
		self.assertNotEqual( 1 + 2, 4 )


class HomePageTest(TestCase):
	def test_home_page_reseolves(self):
		home_page = resolve ('/')
		self.assertEqual(home_page.func, get_index)

	def test_home_page_status_code_is_ok(self):
		home_page = self.client.get('/')
		self.assertEqual(home_page.status_code, 200)

	def test_check_content_is_correct(self):
	       home_page = self.client.get('/')
	       self.assertTemplateUsed(home_page, "index.html")
	       home_page_template_output = render_to_response("index.html").content
	       self.assertEqual(home_page.content, home_page_template_output)
