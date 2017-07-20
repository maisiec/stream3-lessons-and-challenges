from django import forms
from .models import Post

class BlogPostForm(forms.ModelForm): # inherits ModelForm will createinstace of a form when instantiated

	class Meta:
		model = Post   # form is tied to the post model
		fields = ('title', 'content', 'image') #we specify fields to be displayed