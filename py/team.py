
class TeamStats(object):
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        return self.name

    def get_wins(self):
        return float(self.wins)

    def get_losses(self):
        return float(self.losses)

    def get_sos(self):
        return float(self.sos)

    def get_num_inj(self):
        return float(self.num_inj)

    def get_conf(self):
        return float(self.conf)

    def get_rank(self):
        return float(self.rank)

    def get_avg_rush(self):
        return float(self.avg_rush)

    def get_def_rush(self):
        return float(self.avg_def_rush)

    def get_ppg(self):
        return float(self.ppg)
        
    def get_pass_comp(self):
        return float(self.pass_comp)
        
    def get_pass_att(self):
        return float(self.pass_att)
        
    def get_pass_yds(self):
        return float(self.pass_yds)
        
    def get_total_yds(self):
        return float(self.total_yds)
        
    def get_avg_pass_yds(self):
        return float(self.get_pass_yds() / self.get_pass_comp())
        
        
    def import_info(self):
        t1file = "../sets/" + self.name + ".txt"
        with open(t1file) as f:
            lines = f.readlines()

        self.wins             = lines[0].strip()
        self.losses           = lines[1].strip()
        self.conf             = lines[2].strip()
        self.rank             = lines[3].strip()
        self.sos              = lines[4].strip()
        self.num_inj          = lines[5].strip()
        self.avg_rush         = lines[6].strip()
        self.avg_def_rush     = lines[7].strip()
        self.ppg              = lines[8].strip()
        self.pass_comp        = lines[9].strip()
        self.pass_att         = lines[10].strip()
        self.pass_yds         = lines[11].strip()
        self.total_yds        = lines[12].strip()
        
        
class Team(object):
    def __init__(self, name):
        self.team_stats = TeamStats(name)
        self.team_stats.import_info()
        self.has_possession = False
        self.yardline = 0
        self.down = 0
        
    def get_stats(self):
        return self.team_stats
        
    def get_has_possession(self):
        return self.has_possession
        
    def get_down(self):
        return self.down
        
    def set_down(self, down):
        self.down = down
        
    def set_has_possession(self, poss):
        self.has_possession = poss
        
    def get_yardline(self):
        return self.yardline
        
    def set_yardline(self, yl):
        self.yardline = yl

