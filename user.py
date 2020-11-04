import apicalls as a

class User:
    def __init__(self, name, teamName, id):
        self.name = name
        self.teamName = teamName
        self.id = id
        self.gwHistory = a.getUserGWHistory(id)
