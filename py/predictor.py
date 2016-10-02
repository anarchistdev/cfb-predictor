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

    def set_rank(self, rank):
        self.rank = rank

    def set_avgRush(self, rush):
        self.avg_rush = rush

    def set_defRush(self, drush):
        self.avg_def_rush = drush

    def set_ppg(self, ppg):
        self.ppg = ppg

    def get_wins(self):
        return self.wins

    def get_losses(self):
        return self.losses

    def get_sos(self):
        return self.sos

    def get_numInj(self):
        return self.numInj

    def get_conf(self):
        return self.conf

    def get_rank(self):
        return self.rank

    def get_avgRush(self):
        return self.avg_rush

    def get_defRush(self):
        return self.avg_def_rush

    def get_ppg(self):
        return self.ppg

class Predictor(object):
    
    def __init__(self, t1, t2):
        self.t1 = Team(t1)
        self.t2 = Team(t2)
        
    def retrieve_info(self):
        t1file = "../sets/" + self.t1.name + ".txt"
        with open(t1file) as f:
            lines = f.readlines()

        self.t1.set_wins(lines[0].strip())
        self.t1.set_losses(lines[1].strip())
        self.t1.set_conf(lines[2].strip())
        self.t1.set_rank(lines[3].strip())
        self.t1.set_sos(lines[4].strip())
        self.t1.set_numInj(lines[5].strip())
        self.t1.set_avgRush(lines[6].strip())
        self.t1.set_defRush(lines[7].strip())
        self.t1.set_ppg(lines[8].strip())

        t2file = "../sets/" + self.t2.name + ".txt"
        with open(t2file) as f:
            lines2 = f.readlines()

        self.t2.set_wins(lines2[0].strip())
        self.t2.set_losses(lines2[1].strip())
        self.t2.set_conf(lines2[2].strip())
        self.t2.set_rank(lines2[3].strip())
        self.t2.set_sos(lines2[4].strip())
        self.t2.set_numInj(lines2[5].strip())
        self.t2.set_avgRush(lines2[6].strip())
        self.t2.set_defRush(lines2[7].strip())
        self.t2.set_ppg(lines2[8].strip())

        print(self.t2.get_rank())

        print(self.t1.get_rank())


predictor = Predictor(team1, team2)
predictor.retrieve_info()
