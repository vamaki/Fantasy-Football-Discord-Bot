import apicalls as a

class Player:
    def __init__(self, firstName, form, id, cost, ppg, lastName, selectedBy, teamID):
        self.firstName = firstName
        self.form = form
        self.id = id
        self.cost = cost
        self.ppg = ppg
        self.lastName = lastName
        self.selectedBy = selectedBy
        self.teamId = teamID