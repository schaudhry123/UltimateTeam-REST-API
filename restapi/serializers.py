from rest_framework import serializers
from restapi.models import Player, Team
from django.contrib.auth.models import User

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	# team = models.ForeignKey(Team, related_name='players')
	# team = TeamSerializer(read_only=True)
	team_name = serializers.StringRelatedField(source='team', read_only=True)

	class Meta:
		model = Player
		fields = ('id', 'url', 'owner', 'player_name', 'position', 'team', 'team_name', 'nationality', 'player_league')

class TeamSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	players = PlayerSerializer(many=True, read_only=True)

	# players = serializers.StringRelatedField(many=True)
	# players_urls = serializers.HyperlinkedRelatedField(source='players', many=True, read_only=True, view_name='player-detail')

	class Meta:
		model = Team
		fields = ('id', 'url', 'owner', 'team_name', 'manager', 'league', 'players', 'location', 'team_titles')

class UserSerializer(serializers.HyperlinkedModelSerializer):
	players = serializers.HyperlinkedRelatedField(many=True, view_name='player-detail', queryset=Player.objects.all())
	teams = serializers.HyperlinkedRelatedField(many=True, view_name='team-detail', queryset=Team.objects.all())

	class Meta:
		model = User
		fields = ('id', 'url', 'username', 'players', 'teams')