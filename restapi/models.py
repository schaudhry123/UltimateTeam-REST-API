from django.db import models

# Create your models here.
class Team(models.Model):
	id = models.AutoField(primary_key=True)
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

class Player(models.Model):
	id = models.AutoField(primary_key=True)
	player_name = models.CharField(max_length=100, null=True)
	position = models.CharField(max_length=3, null=True)
	team = models.ForeignKey(Team, on_delete=models.CASCADE, default="", related_name='players', null=False)
	nationality = models.CharField(max_length=100, null=True)
	player_league = models.CharField(max_length=100, null=True)
	owner = models.ForeignKey('auth.User', related_name='players', default=0)

	class Meta:
		ordering = ["player_name"]

	def __str__(self):
		return str(self.player_name)
