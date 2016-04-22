from rest_framework import serializers
from restapi.models import Player, Team, User

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
	#owner = serializers.ReadOnlyField(source='owner.username')
	#team = models.ForeignKey(Team, related_name='players')
	#team = TeamSerializer(read_only=True)
	team_name = serializers.StringRelatedField(source='team', read_only=True)

	class Meta:
		model = Player
		fields = ('id', 'url', 'name', 'year', 'team', 'player_league', 'team_name', 'position', 'age', 'height', 'weight', 'appearances', 'goals', 'assists', 'yellow', 'red', 'shots_per_game', 'ps', 'aerials_won', 'position', 'motm', 'rating', 'skills')

class TeamSerializer(serializers.HyperlinkedModelSerializer):
	#owner = serializers.ReadOnlyField(source='owner.username')
	players = PlayerSerializer(many=True, read_only=True)

	# players = serializers.StringRelatedField(many=True)
	# players_urls = serializers.HyperlinkedRelatedField(source='players', many=True, read_only=True, view_name='player-detail')

	class Meta:
		model = Team
		fields = ('id', 'url', 'username', 'name', 'league', 'players')

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username')

