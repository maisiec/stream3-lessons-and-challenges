# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from views import profile
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from .models import User
from .forms import UserRegistrationForm
from django import forms
from django.conf import settings
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

	def test_registration_form(self):
		form = UserRegistrationForm({
			'email': 'test@test.com',
			'password1': 'letmein',
			'password2': 'letmein',
			'stripe_id': settings.STRIPE_SECRET,
			'credit_card_number': 4242424242424242,
			'cvv': 123,
			'expiry_month': 1,
			'expiry_year': 2033
			})

		self.assertTrue(form.is_valid())

	def test_registration_form_fails_with_missing_email(self):
		form = UserRegistrationForm({
			'password1':'letmein',
			'password2':'letmein',
			'stripe_id': settings.STRIPE_SECRET,
			'credit_card_number': 4242424242424242,
			'cvv': 123,
			'expiry_month': 1,
			'expiry_year': 2033
			})

		self.assertFalse(form.is_valid())
		self.assertRaisesMessage(forms.ValidationError, "Please enter your email address", form.full_clean())

	def test_registration_fails_with_empty_password1(self):
		form = UserRegistrationForm({
			'password2':'letmein',
			'stripe_id': settings.STRIPE_SECRET,
			'credit_card_number': 4242424242424242,
			'cvv': 123,
			'expiry_month': 1,
			'expiry_year': 2033
			})

		self.assertFalse(form.is_valid())
		self assertRaisesMessage(forms.ValidationError,"passwords do not match", form.full_clean())

	def test_registration_fails_with_empty_password2(self):
		form = UserRegistrationForm({
			'password1':'letmein',
			'stripe_id': settings.STRIPE_SECRET,
			'credit_card_number': 4242424242424242,
			'cvv': 123,
			'expiry_month': 1,
			'expiry_year': 2033
			})

		self.assertFalse(form.is_valid())
		self assertRaisesMessage(forms.ValidationError,"passwords do not match", form.full_clean())

	def test_registraion_form_fails_with_passwords_that_dont_match(self):
		form = UserRegistrationForm({
			'password1':'letmein',
			'password2':'letmein1',
			'stripe_id': settings.STRIPE_SECRET,
			'credit_card_number': 4242424242424242,
			'cvv': 123,
			'expiry_month': 1,
			'expiry_year': 2033
			})

		self.assertFalse(form.is_valid())
		self.assertRaisesMessage(forms.ValidationError, "passwords do not match", form.full_clean())
