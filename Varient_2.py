from Strategy import StrategyBase
from scipy.optimize import root_scalar
import numpy as np

def equation(x, X, n):
    term1 = x**(n - 1) * (1 - 11 * n)
    term2 = x**(n - 2) * (11 * n * X - 11 * X)
    term3 = 100**(n - 1)
    return term1 + term2 + term3

class UserStrategy(StrategyBase):

    def make_bid(self, current_value, previous_winners, previous_second_highest_bids, capital, num_bidders):
        X_val = current_value
        n_val = num_bidders

        try:
            sol = root_scalar(equation, args=(X_val, n_val), bracket=[0.01, 100], method='brentq')
            if sol.converged:
                root = sol.root
                min_bid = 100 / (11 ** (1 / (n_val - 1)))  
                if min_bid < root < X_val:
                    return (root, 1)
                else:
                    return (0, 0)
            else:
                return (0, 0)
        except:
            return (0, 0)
