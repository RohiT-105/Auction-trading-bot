from Strategy import StrategyBase

def expected_max_given_x(x, n):
    total = 0.0
    for y in range(x + 1, 101):
        prob = ((y + 1) / 101) ** (n - 1) - (y / 101) ** (n - 1)
        total += y * prob
    total += x * ((x + 1) / 101) ** (n - 1)
    return total
class UserStrategy(StrategyBase):

    # Refer to Strategy.py for implementation details
    # Edit the function below without changing its template(name, input parameters, output type)
    def make_bid(self, current_value, previous_winners,previous_second_highest_bids,capital,num_bidders):
        # Example strategy: Bid a constnant amount = 50

        # return (50, 0.75) # return a tuple (bid, confidence) only for variant 2, where a confidence is also needed
        return (current_value-1,1)  # return a single value (only bid) for variants 1 & 3, as confidence is not required here
       
        