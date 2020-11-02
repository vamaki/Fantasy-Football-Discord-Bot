import requests
import json
import player as p

def createPlayers(leagueID):
    url = 'https://fantasy.premierleague.com/api/leagues-classic/{ID}/standings/'.format(ID = leagueID)
    league = json.loads(requests.get(url).text)
    players = []
    for team in league["standings"]["results"]:
        name = team["player_name"]
        teamName = team["entry_name"]
        id = team["entry"]
        player = p.Player(name, teamName, id)
        players.append(player)

    return players

def getLeagueStandings(leagueID):
    url = 'https://fantasy.premierleague.com/api/leagues-classic/{ID}/standings/'.format(ID = leagueID)
    league = json.loads(requests.get(url).text)
    for team in league["standings"]["results"]:
        print(team["entry_name"] + "\t\t" + str(team["total"]))

def chipsPlayed():
    url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
    data = json.loads(requests.get(url).text)
    for gameweek in data["events"]:
        if(gameweek["finished"]):
            print(gameweek["name"])
            for chip in gameweek["chip_plays"]:
                print(chip["chip_name"] + ": " + str(chip["num_played"]))
            print()
        else:
            break

def getPlayerGWHistory(playerID):
    url = 'https://fantasy.premierleague.com/api/entry/{ID}/history/'.format(ID = playerID)
    player = json.loads(requests.get(url).text)
    history = []
    for gameweek in player["current"]:
        history.append(gameweek["points"])

    return history
