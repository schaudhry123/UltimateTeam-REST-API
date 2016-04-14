from rest_framework import serializers
from restapi.models import Team
from django.contrib.auth.models import User

class TeamSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Team
		fields = ('id', 'owner', 'team_name', 'manager', 'league', 'location', 'team_titles')

class UserSerializer(serializers.ModelSerializer):
	teams = serializers.PrimaryKeyRelatedField(many=True, queryset=Team.objects.all())

	class Meta:
		model = User
		fields = ('id', 'username', 'teams')