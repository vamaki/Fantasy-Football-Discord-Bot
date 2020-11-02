import apicalls as a

players = a.createPlayers('1243733')

for player in players:
    print(player.teamName)
    i = 1
    for gw in player.gwHistory:
        print("GW" + str(i) + ": " + str(gw))
        i+=1
    print()