from django.db import models

# Create your models here.
class Team(models.Model):
	team_name = models.CharField(max_length=100, null=True)
	manager = models.CharField(max_length=100, null=True)
	league = models.CharField(max_length=100, null=True)
	location = models.CharField(max_length=100, null=True)
	team_titles = models.IntegerField(default=0, null=True)
	owner = models.ForeignKey('auth.User', related_name='teams', default=0)

	class Meta:
		ordering = ["league", "team_name"]

	# For printing string
	def __str__(self):
		return str(self.team_name)

	# Has won any titles
	def has_won_titles(self):
		return self.team_titles > 0