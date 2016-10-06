from team import Team
import sys

import random

t1 = sys.argv[1]
t2 = sys.argv[2]

class Possession(object):
    # @param t1 - the Team class of the offense
    # @param t2 - the Team class of the defense
    def __init__(self, t1, t2):
        self.offense = t1
        self.defense = t2
        
    # For now, this function will just base the eqation on the % of pass plays
    # In the future, it should take into consideration the down and yardage
    def should_pass(self):
        totalRushYds = self.offense.get_stats().get_total_yds() - self.offense.get_stats().get_pass_yds()
        print(totalRushYds)
        
    # Return for boolean:
    #   True if the team scored
    #   False if the team didn't
    def drive(self):
        while (self.offense.get_down() < 4):
            self.should_pass()
            self.offense.set_down(4)


class Game(object):
    # @param t1 - name of team1
    # #param t2 - name of team2
    def __init__(self, t1, t2):
        self.verbose = False
        self.team1 = Team(t1)
        self.team2 = Team(t2)
        
        
    def set_verbose(self, v):
        self.verbose = v
        
    # Not actual coin toss simulation, just crude random 1st possession
    # TODO - real coin sim
    def coin_toss(self):
        coin = random.randint(0,1)
        if (coin == 0):
            self.team1.set_has_possession(True)
            if (self.verbose):
                print(self.team1.get_stats().get_name() + " has won the coin toss!")
        elif (coin == 1):
            self.team2.set_has_possession(True)
            if (self.verbose):
                print(self.team2.get_stats().get_name() + " has won the coin toss!")
            
            
            
    def simulate(self):
        self.coin_toss()
        
        if (self.team1.get_has_possession()):
            possession = Possession(self.team1, self.team2)
            possession.drive()
            
    
    

game = Game(t1, t2)
game.set_verbose(True)

game.simulate()
