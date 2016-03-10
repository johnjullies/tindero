from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
	user = models.OneToOneField(User)

	photo = models.ImageField(upload_to='photos')
	bio = models.TextField()

	def __unicode__(self):
		return self.user.get_full_name()


class UserVote(models.Model):
	user = models.ForeignKey(User)
	voter = models.ForeignKey(User, related_name='given_vote')
	vote = models.BooleanField(default=False)

	class Meta:
		unique_together = (('user', 'voter'))
		