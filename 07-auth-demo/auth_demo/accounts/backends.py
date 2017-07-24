# This file will hold our code to check if the email and password are correct,
# and also to allow/disallow login:

from models import User 

class EmailAuth(object)

	def authenticate(self, email=None, password=None):
		"""
		Get an instance of User using the supplied email and check its password
		"""
		try:
			user=User.objects.get(email=email)
			if user.check_password(password):
				return user

		except User.DoesNotExist:
			return None

	def get_user(self, user_id):
		"""
		Used by the django authentication sysytem to retrieve an instance of User
		"""
		try:
			user=User.objects.get(pk=user_id)
			if user.is_active:
				return user
			return None
		except User.DoesNotExist:
			return None

# Here we've created a class that will replace the standard 'auth'
# object that django uses to check logins and we override two of 
# its default methods. 

# This is actually not that different from the default method for
# testing against the username field. 
# We’ve simply swapped out the username field for the email field.