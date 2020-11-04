import apicalls as a

users = a.createUsers('1243733')

for user in users:
    print(user.teamName)
    i = 1
    for gw in user.gwHistory:
        print("GW" + str(i) + ": " + str(gw))
        i+=1
    print()