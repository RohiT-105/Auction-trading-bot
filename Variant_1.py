from Strategy import StrategyBase
from sympy import symbols, Eq, solve, simplify
import numpy as np
  
def expected_max_given_x(x, n):
    total = 0.0
    for y in range(x + 1, 101):
        prob = ((y + 1) / 101) ** (n - 1) - (y / 101) ** (n - 1)
        total += y * prob
    total += x * ((x + 1) / 101) ** (n - 1)
    return total

class UserStrategy(StrategyBase):

    def make_bid(self, current_value, previous_winners,previous_second_highest_bids,capital,num_bidders):        
        x = symbols('x')
        X_val = expected_max_given_x (current_value,num_bidders)
        n_val = num_bidders
        a = (x) / 100
        b = (100 - x) / 100

        # differential equation to maximize payoff considering being placed in 2nd position alsp
        # dpdx = - (a**(n_val - 1) + (n_val - 1) * a**(n_val - 2) * b) \
        #     + (X_val - x) * (
        #             (n_val - 1)/100 * a**(n_val - 2)
        #             + (n_val - 1)*(n_val - 2)/100 * a**(n_val - 3) * b
        #             - (n_val - 1)/100 * a**(n_val - 2)
        #     )
        optimal = X_val - (X_val/(n_val)) #optimal for being placed 1st
        if previous_winners and capital>200:
            filtered_winners = [w for w in previous_winners if w <= X_val]
            if filtered_winners:
                avg_prev_winner = sum(filtered_winners) / len(filtered_winners)
            else:
                avg_prev_winner = None
        else:
            avg_prev_winner = None
        if previous_winners:
            if avg_prev_winner:
                return (avg_prev_winner*(n_val) +X_val)/(n_val+1)
            # dpdx = - (a**(n_val - 1)) + (X_val - x) * ((n_val - 1) / 100) * a**(n_val - 2)
            else:
                return optimal
        else:
            low = expected_max_given_x (0,num_bidders)
            return low - (low/(n_val))
        #     if avg_prev_winner:
        #         if (avg_prev_winner+(X_val - (X_val/(n_val))))/2 <= X_val:
        #             return (avg_prev_winner+(X_val - (X_val/(n_val))))/2
        #         else: 
        #             return X_val-0.5
        #     return ((X_val - (X_val/(n_val)))*(n_val-1) + X_val)/n_val
    
        
        
