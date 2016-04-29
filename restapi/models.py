from django.db import models

# Create your models here.
class User(models.Model):
	id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=100, null=False)

	# For printing string
	def __str__(self):
		return str(self.username)	

class Player(models.Model):
	id = models.AutoField(primary_key=True)
	year = models.CharField(max_length = 4, null=True)
	#player_league = models.CharField(max_length=100, null=True)
	#team = models.ForeignKey(Team, on_delete=models.CASCADE, default=0, related_name='players', null=False)
	name = models.CharField(max_length=100, null=True)
	age = models.CharField(max_length=3, null=True)
	position = models.CharField(max_length=20, null=True)
	height = models.CharField(max_length=3, null=True)
	weight = models.CharField(max_length=3, null=True)
	appearances = models.CharField(max_length=5, null=True)
	goals = models.CharField(max_length=3, null=True)
	assists = models.CharField(max_length=3, null=True)
	yellow = models.CharField(max_length=3, null=True)
	red = models.CharField(max_length=3, null=True)
	shots_per_game = models.CharField(max_length=3, null=True)
	ps = models.CharField(max_length=5, null=True)
	aerials_won = models.CharField(max_length=5, null=True)
	motm = models.CharField(max_length=3, null=True)
	rating = models.CharField(max_length=10, null=True)
	skills = models.CharField(max_length=20, null=True)

	#owner = models.ForeignKey('auth.User', related_name='players', default=0)

	class Meta:
		ordering = ["name"]

	def __str__(self):
		return str(self.name)

class Team(models.Model):
	id = models.AutoField(primary_key=True)
	league = models.CharField(max_length=100, null=True)
	name = models.CharField(max_length=100, null=True)
	username = models.CharField(max_length=100, null=True)

	players = models.ManyToManyField(Player, related_name='teams')

	class Meta:
		ordering = ["league", "name"]

	# For printing string
	def __str__(self):
		return str(self.name)


