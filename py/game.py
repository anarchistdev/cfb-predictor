from team import Team
import sys

import random

t1 = sys.argv[1]
t2 = sys.argv[2]

class Logger:
    @staticmethod
    def log_yds(name, yds, did_pass):
        if (did_pass):
            print(str(name) + " passed for a gain of " + str(yds) + " yards!")
        else:
            if (yds < 0):
                print(name + "'s rb tackled in the backfield for a loss of " + str(abs(yds)) + " yards!")
            else:
                print(str(name) + " ran for a gain of " + str(yds) + " yards!")
    
    @staticmethod
    def log_first_down(name):
        print(name + " gained a first down!")
        
    def log_down(down):
        print("Down: " + str(down))
        
    @staticmethod
    def log_incomplete():
        print("Incomplete Pass! 0 yards gained.")
        
    @staticmethod
    def log(text):
        print(text)

class Possession(object):
    # @param t1 - the Team class of the offense
    # @param t2 - the Team class of the defense
    def __init__(self, t1, t2, verbose):
        self.offense = t1
        self.defense = t2
        self.verbose = verbose
        self.first_down = 30 # By default, the offense starts on the 20 yardline. So the first down would be yardline+10

    # TODO - fix the return statement
    def should_pass(self):
        total_rush_yds = self.offense.get_stats().get_total_yds() - self.offense.get_stats().get_pass_yds()
        total_pass_yds = self.offense.get_stats().get_pass_yds()
        passPct = (total_pass_yds / self.offense.get_stats().get_total_yds()) * 100

        if (self.offense.get_down() == 1):
            passPct += random.randint(-8, 8)
        elif (self.offense.get_down() == 2):
            passPct += random.randint(2, 6)
            if (self.offense.get_distance() <= 5):
                passPct -= random.randint(-2, 6)
        elif (self.offense.get_down() == 3):
            passPct += random.randint(3, 12)
            if (self.offense.get_distance() <= 3):
                passPct -= random.randint(25, 45)
            elif (self.offense.get_distance() > 4):
                passPct += random.randint(3, 12)
                
        return (passPct)>=50
        
        
    def calc_pass_comp(self):
        pass_pct = (self.offense.get_stats().get_pass_comp() / self.offense.get_stats().get_pass_att()) * 100
        return pass_pct
        
        
    # Calculates the yardline, down, and distance for each play
    def play(self):
        yards_gained = 0
        
        should_pass = self.should_pass()
        if (should_pass):
            # Use the pass comp to determine if the pass is incomplete
            yards_gained = random.randint(1, int(self.offense.get_stats().get_avg_pass_yds()+(self.offense.get_stats().get_avg_pass_yds()/2)))
            
        else :
            # TODO - use the defenses rush stats to balance it out
            yards_gained = random.randint(-5, int(self.offense.get_stats().get_avg_rush_yds()+(self.offense.get_stats().get_avg_rush_yds()/2)))
            
            
        self.offense.add_yards(yards_gained)
        if (self.verbose):
            Logger.log_yds(self.offense.get_stats().get_name(), yards_gained, should_pass)
            
        if (self.offense.get_yardline() >= self.first_down): # If the team gets the first down
            self.offense.set_first_down()
            self.first_down = self.offense.get_yardline() + 10 # Increase the distance to the first down
            if (self.verbose):
                Logger.log_first_down(self.offense.get_stats().get_name())
        else: # If they fail to get the first down
            self.offense.set_down(self.offense.get_down() + 1) # Increase the down
            if (self.verbose):
                Logger.log_down(self.offense.get_down()) 
            
        if (self.offense.get_yardline() >= 100): # If they score a touchdown
            self.offense.add_points(7)
            if (self.verbose):
                Logger.log("Touchdown!")
                Logger.log("Yardline: " + str(self.offense.get_yardline()))
        
    # Returns the amount of points scored, if any
    def drive(self):
        if (self.verbose):
            Logger.log("New Possession ----------------------------")
            
        self.offense.set_first_down()
        self.offense.set_yardline(20)
        while (self.offense.get_yardline() < 100):
            self.play()
            if (self.offense.get_down() >= 4):
                break


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
        if (self.team1.get_has_possession()):
            possession = Possession(self.team1, self.team2, self.verbose)
            possession.drive()
            self.team2.set_has_possession(True)
            self.team1.set_has_possession(False)
            
        elif (self.team2.get_has_possession()):
            possession = Possession(self.team2, self.team1, self.verbose)
            possession.drive()
            self.team1.set_has_possession(True)
            self.team2.set_has_possession(False)
            
        self.finalize()
        self.simulate()
        
    def finalize(self):
        if (self.verbose):
            Logger.log(self.team1.get_stats().get_name() + " " + str(self.team1.get_points()))
            Logger.log(self.team2.get_stats().get_name() + " " + str(self.team2.get_points()))
            
    
    

game = Game(t1, t2)
game.set_verbose(True)

game.coin_toss()
game.simulate()
