from enum import Enum
import numpy as np


class OutcomesCoin(Enum):
    #  heads vs tails
    Heads = 1
    Tails = 0


class Game:
    def __init__(self):
       # self._id = id
        self._rnd = np.random
        #self._rnd.seed(id)
        self._headsProb = headsProb
        self._outcomes = []  # create empty list to store outcomes
        self._flip =[] #outcome of one toss

    def simulate(self):

        t = 0  # simulation time

        # flipping the coin
        while t < 20:  # number of flips is 20
            # determine what the flip is
            if self._rnd.sample() < self._headsProb:
                self._flip = OutcomesCoin.Heads
            else:
                self._flip = OutcomesCoin.Tails
            self._outcomes.append(self._flip.name)
            # increment time
            t += 1

    def get_expected_reward(self):
        countWins = " ".join(map(str,self._outcomes))
        win = countWins.count(winning_series)
        total_payout = (win * 100) - 250
        return total_payout


winning_series = "Tails Tails Heads"
headsProb =0.5
trials = 1000

trial1 = Game()
print(trial1.get_expected_reward())




class Cohort:
    def __init__(self, trials):
        self.listgames = []  # list of games
        self.reward = []  # list of rewards
        self._numTrials = trials

        # add games to the cohort
        for i in range(trials):
            game = Game()
            self.listgames.append(game)

    def play(self):
        for game in self.listgames:

            game.simulate()

            value = Game.get_expected_reward()
            self.reward.append(value)

    def get_ave_expected_reward(self):
        return sum(self.reward)/len(self.reward)


MyCohort = Cohort(trials= 1000)
print(MyCohort.get_ave_expected_reward())

#MyGame = Game(id=1, heads_prob=0.5)
#print(MyGame.simulate())
#print(MyGame.get_expected_reward())



test = OutcomesCoin.Heads
