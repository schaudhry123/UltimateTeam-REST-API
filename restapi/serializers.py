from rest_framework import serializers
from restapi.models import Player, Team
from django.contrib.auth.models import User

class TeamSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	players = serializers.StringRelatedField(many=True)

	class Meta:
		model = Team
		fields = ('url', 'owner', 'team_name', 'manager', 'league', 'players', 'location', 'team_titles')

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	# team = models.ForeignKey(Team, related_name='players')
	# team = TeamSerializer(read_only=True)
	team_name = serializers.StringRelatedField(source='team', read_only=True)

	class Meta:
		model = Player
		fields = ('url', 'owner', 'player_name', 'position', 'team', 'team_name', 'nationality', 'player_league')

class UserSerializer(serializers.HyperlinkedModelSerializer):
	players = serializers.HyperlinkedRelatedField(many=True, view_name='player-detail', queryset=Player.objects.all())
	teams = serializers.HyperlinkedRelatedField(many=True, view_name='team-detail', queryset=Team.objects.all())

	class Meta:
		model = User
		fields = ('url', 'username', 'players', 'teams')