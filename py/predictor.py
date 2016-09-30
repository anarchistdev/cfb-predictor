import sys

team1 = sys.argv[1]
team2 = sys.argv[2]

class Team(object):
    def __init__(self, name):
        self.name = name
        
    def set_wins(self, wins):
        self.wins = wins
        
    def set_losses(self, losses):
        self.losses = losses
        
    def set_sos(self, sos):
        self.sos = sos
        
    def set_numInj(self, inj):
        self.numInj = inj
        
    def set_conf(self, conf):
        self.conf = conf

class Predictor(object):
    
    def __init__(self, t1, t2):
        self.t1 = Team(t1)
        self.t2 = Team(t2)
        
    def retrieveInfo(self):
        t1file = "../sets/" + self.t1.name + ".txt"
        with open(t1file) as f:
            lines = f.readlines()

        print(lines)


predictor = Predictor(team1, team2)
predictor.retrieveInfo()
