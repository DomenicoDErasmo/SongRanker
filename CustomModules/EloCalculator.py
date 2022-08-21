import math


# Function to calculate the Probability
def Probability(loser_rating, winner_rating):
    """
    Calculates the probability of one player winning versus another based on the difference on their ELO scores.

    Keyword Arguments:
        loser_rating -- The rating of the losing player.
        winner_rating -- The rating of the winning player.

    Returned Values:
        probability -- The odds that the winning player would win the match.
    """
    probability = 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (loser_rating - winner_rating) / 400))
    return probability


def UpdateEloRating(rating_a, rating_b, k_value, winner):
    """
    Updates the new ELO scores for each song.

    Keyword Arguments:
        rating_a -- The rating of the first song.
        rating_b -- The rating of the second song.
        K -- A variance coefficient used in ELO calculations. A higher K value leads to bigger ELO changes.
        winner -- The winning song, expressed as 1 for the first song and any other integer for the second song.

    Returned Values:
        probability -- The odds that the winning player would win the match.
    """
    probability_b_wins = Probability(rating_a, rating_b)
    probability_a_wins = Probability(rating_b, rating_a)

    # Case 1: When Player A wins
    if winner == 1:
        rating_a = rating_a + k_value * (1 - probability_a_wins)
        rating_b = rating_b + k_value * (0 - probability_b_wins)

    # Case 2: When Player B wins
    else:
        rating_a = rating_a + k_value * (0 - probability_a_wins)
        rating_b = rating_b + k_value * (1 - probability_b_wins)

    rating_a = round(rating_a, 2)
    rating_b = round(rating_b, 2)

    return rating_a, rating_b
