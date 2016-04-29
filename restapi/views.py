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
        team1 = Team.objects.get(pk = pk1)
        #team1 = get_players(team)
        team2 = Team.objects.get(pk = pk2)
        winning_team = sim2.compare_teams(team1, team2)
        #team2 = get_players(team)
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

def get_players(team):
    players = []
    players_url = team.players.all()
    for url in players_url:
        pk = get_pk(url)
        players.append(Player.objects.get(pk = pk))
    return players

def get_pk(url):
    start = end = 0
    num_slash = 0
    idx = 0
    reverse = url[::-1]
    for c in reverse:
        if(c == '/'):
            num_slash+=1
        if(num_slash == 1):
            start = idx
            num_slash = 2
        if(num_slash == 3):
            end = idx
            break
        idx+=1
    return int((reverse[start+1:end])[::-1])






