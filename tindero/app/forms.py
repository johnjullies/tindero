from django.forms import ModelForm

from . import models


class UserProfileForm(ModelForm):
	class Meta:
		model = models.UserProfile
		exclude = ('user',)