from enum import Enum
import numpy as np


class OutcomesCoin(Enum):
    #  heads vs tails
    Heads = 1
    Tails = 0


class Game:
    def __init__(self, id, headsProb):
        self._id = id
        self._rnd = np.random
        self._headsProb = headsProb
        self._outcomes = []  # create empty list to store outcomes
        self._flip = []  # outcome of one toss

    def simulate(self):

        t = 0  # simulation time

        # flipping the coin
        while t < 20:  # number of flips is 20
            # determine what the flip is
            if self._rnd.sample() < self._headsProb:
                self._flip = OutcomesCoin.Heads
                self._outcomes.append('Heads')
            else:
                self._flip = OutcomesCoin.Tails
                self._outcomes.append('Tails')
            # increment time
            t += 1

    def get_expected_reward(self):
        countwins = " ".join(map(str,self._outcomes))
        win = countwins.count(winning_series)
        total_payout = (win * 100) - 250
        return total_payout


winning_series = "Tails Tails Heads"
headsProb = 0.4


class Cohort:
    def __init__(self, probtrials, headsProb):
        self._gameRewards = []  # list of rewards

        # add games to the cohort
        for n in range(probtrials):
            new_game = Game(id=n, headsProb=headsProb)
            new_game.simulate()
            self._gameRewards.append(new_game.get_expected_reward())

    def get_ave_expected_reward(self):
        return sum(self._gameRewards)/len(self._gameRewards)


trial = Cohort(headsProb=0.4, probtrials=1000)
print('When the probability of flipping heads is', headsProb,
      'the expected reward:', trial.get_ave_expected_reward())
