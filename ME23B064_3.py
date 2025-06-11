from Strategy import StrategyBase
from sympy import symbols, diff, Eq, solve, simplify
  
def expected_max_given_x(x, n):
    total = 0.0
    for y in range(x + 1, 101):
        prob = ((y + 1) / 101) ** (n - 1) - (y / 101) ** (n - 1)
        total += y * prob
    total += x * ((x + 1) / 101) ** (n - 1)
    return total

class UserStrategy(StrategyBase):

    def make_bid(self, current_value, previous_winners, previous_second_highest_bids, capital, num_bidders):        
        x, X, k, n = symbols('x X k n', real=True, positive=True)

        a = (x / 100)
        b = ((100 - x) / 100)
        term1 = a ** (n - 1) * (X - x - k)
        term2 = (n - 1) * a ** (n - 2) * b * 0.5 * (X - x - k)
        f = term1 - term2

        dfdx = simplify(diff(f, x))

        X_val = expected_max_given_x(current_value, num_bidders)
        n_val = num_bidders

        # Filtered average k: only include winner-second pairs where winner < X_val
        if previous_winners and previous_second_highest_bids and len(previous_winners) == len(previous_second_highest_bids):
            diffs = [
                a - b for a, b in zip(previous_winners, previous_second_highest_bids) if a < X_val
            ]
            k_val = sum(diffs) / len(diffs) if diffs else 0
        else:
            k_val = 0

        if capital<350:
            X_val = current_value

        dfdx_sub = dfdx.subs({X: X_val, k: k_val, n: n_val})

        roots = solve(Eq(dfdx_sub, 0), x)
        real_roots = [r.evalf() for r in roots if r.is_real and 0 <= r <= X_val]

        bid = max(real_roots) if real_roots else 0
        return float(bid)

    
        
        