import math
import random
import requests

def compare_teams(team1, team2):
    result = {}

    team1_chance = {}
    team2_chance = {}
    team1_players = team1.players.all()
    team2_players = team2.players.all()
    
    #get the aggregrate elo 
    team1_elo = get_elo(team1_players)
    team2_elo = get_elo(team2_players)
    
    #find the multiplier for the supposed goal differential
    #for every 10 points of elo difference, there should be a 1 to 2 goal gap
    multiplier = (random.uniform(0.2, 1.4) * 2.0)
    
    #if they are within 10 points of elo, then i want to make the winner random, goal diff constant
    elo_diff = abs(team1_elo - team2_elo)
    if(elo_diff <= 10):
        winner = math.floor(random.uniform(0.0, 2.0))
    elif(team1_elo > team2_elo):
        winner = 0
    else:
        winner = 1
    
    #find difference in elo between two teams in increments of 10
    elo_diff = math.ceil(abs(team1_elo - team2_elo)/10)
 
    goal_diff = math.floor(elo_diff*multiplier)
    
    #assuming everyone is sportsmanlike and won't go to double digits
    if(goal_diff > 10):
        goal_diff = 9
    
    #the losers goals will have an exponential distribution with mean 5/4
    l_goals = math.floor(random.expovariate(0.8))
    #winners goals is goal differential plus l_goals
    w_goals = goal_diff + l_goals
    
    if(winner == 1):
        one_scorers = get_scorers(team1_players, l_goals)
        two_scorers = get_scorers(team2_players, w_goals)
        results['winning_score'] = w_goals
        results['winning_team'] = team2.name
        results[team1.name] = one_scorers
        results['losing_score'] = l_goals
        results['losing_team'] = team1.name
        results[team2.name] = two_scorers
    else:
        one_scorers = get_scorers(team1_players, w_goals)
        two_scorers = get_scorers(team2_players, l_goals)
        results['winning_score'] = w_goals
        results['winning_team'] = team1.name
        results[team1.name] = one_scorers
        results['losing_score'] = l_goals
        results['losing_team'] = team2.name
        results[team2.name] = two_scorers


'''
gets the aggregate elo of a team
@param
    players on a team list
@return
    aggregate elo of team
'''
def get_elo(team_players):
    total_elo =0.0
    for player in team_players:
        total_elo += float(player.rating)
    return total_elo

'''
gets scorers for a team
@param 
    list of player dicts
    number of goals scored by team
@return 
    dict with structure
        player.name: number of goals
'''
def get_scorers(players, goals):
    scorers = {}
    pr = sorted(players, key=lambda player:players.rating)
    for player in pr:
        if goals != 0:
            scorers[player.name] = math.floor(random.uniform(1, 3))
            goals -= scorers[player.name]
        else:
            break
    return scorers