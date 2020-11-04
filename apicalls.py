import requests
import json
import user as u
import player as p


# Some urls that are needed in development still
# https://fantasy.premierleague.com/api/entry/{TEAMID}/transfers/ + latest
# https://fantasy.premierleague.com/api/entry/{USERID}/event/3/picks/
# https://fantasy.premierleague.com/api/element-summary/{PLAYERID}/

def createPlayer(playerID):
    url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
    data = json.loads(requests.get(url).text)
    for player in data["elements"]:
        if player["id"] == playerID:
            print("foundz")
            firstName = player["first_name"]
            form = player["form"]
            id = player["id"]
            cost = player["now_cost"]
            ppg = player["points_per_game"]
            lastName = player["second_name"]
            selectedBy = player["selected_by_percent"]
            teamID = player["team"]
            createdPlayer = p.Player(firstName, form, id, cost, ppg, lastName, selectedBy, teamID)
            break

    return createdPlayer

def createUsers(leagueID):
    url = 'https://fantasy.premierleague.com/api/leagues-classic/{ID}/standings/'.format(ID = leagueID)
    league = json.loads(requests.get(url).text)
    users = []
    for team in league["standings"]["results"]:
        name = team["player_name"]
        teamName = team["entry_name"]
        id = team["entry"]
        user = u.User(name, teamName, id)
        users.append(user)

    return users

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

def getUserGWHistory(userID):
    url = 'https://fantasy.premierleague.com/api/entry/{ID}/history/'.format(ID = userID)
    user= json.loads(requests.get(url).text)
    history = []
    for gameweek in user["current"]:
        history.append(gameweek["points"])

    return history
