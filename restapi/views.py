from restapi.models import Team, Player, User
from rest_framework.decorators import api_view
from rest_framework import viewsets
from restapi.serializers import PlayerSerializer, TeamSerializer, UserSerializer
from django.core import serializers
from rest_framework.response import Response
#from restapi.permissions import IsOwnerOrReadOnly, IsAnonCreate
import simulator
import sim2

class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    #permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

@api_view(['GET'])
def get_simulation(request, pk1, pk2):
    """
    Get team simulation
    """
    try:
        team1 = Team.objects.get(pk=pk1)
        team2 = Team.objects.get(pk = pk2)
        winning_team = sim2.compare_teams(team1, team2)
        print(winning_team)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        #obj_as_json = serializers.serialize("json", winning_team)
        #serializer = ResultSerializer(avg_user)
        return Response(winning_team)

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
