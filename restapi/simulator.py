import math
import random

def compare_teams(team1, team2):
    result = {}

    team1_chance = {}
    team2_chance = {}
    team1_players = team1.players.all()
    team2_players = team2.players.all()
    team1_keep = 1
    team2_keep = 1
    for player in team1_players:
        if(player.position != 'Keeper'):
            conversion = float(player.goals)/max(1, float(player.appearances))
            spg = float(player.shots_per_game)
            team1_chance[player.name] = conversion/spg * random.uniform(1, 1.5)
        else:
            team1_keep = 10.0 - random.uniform(0.5, 1) * float(player.rating)
            
    for player in team2_players:
        if(player.position != 'Keeper'):
            conversion = float(player.goals)/max(1, float(player.appearances))
            spg = float(player.shots_per_game)
            team2_chance[player.name] = conversion/spg * random.uniform(1, 1.5)
        else:
            team2_keep = 10.0 - random.uniform(0.5, 1) * float(player.rating)
 
    one_scorers = {}
    two_scorers = {}
    team1_goals = 0
    team2_goals = 0
 
    for player in team1_chance:
        goals = math.floor(team1_chance[player] * team2_keep)
        if(goals >= 1):
            team1_goals += goals
            one_scorers[player] = goals
    for player in team2_chance:
        goals = math.floor(team2_chance[player] * team1_keep)
        if(goals >= 1):
            team2_goals += goals
            two_scorers[player] = goals

    results = {}

    if team1_goals > 4:
        team1_goals = 4
    if team2_goals > 4:
        team2_goals = 4

    if team1_goals > team2_goals:
        results['winning_score'] = team1_goals
        results['winning_team'] = team1.name
        results[team1.name] = one_scorers
        results['losing_score'] = team2_goals
        results['losing_team'] = team2.name
        results[team2.name] = two_scorers
    else:
        results['winning_score'] = team2_goals
        results['winning_team'] = team2.name
        results[team1.name] = one_scorers
        results['losing_score'] = team1_goals
        results['losing_team'] = team1.name
        results[team2.name] = two_scorers

    return results