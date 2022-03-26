# pylint: disable=missing-docstring

import csv

COUNTRIES_FILEPATH = "data/dictionary.csv"
MEDALS_FILEPATH = "data/winter.csv"


def most_decorated_athlete_ever():
    """Returns who won the most winter olympic games medals (gold/silver/bronze) ever"""
    # Create a winter olypmics list of dictionary
    medal_count = {}
    with open(MEDALS_FILEPATH, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["Athlete"] in medal_count.keys():
                medal_count[row["Athlete"]] +=1
            else:
                medal_count[row["Athlete"]] = 1

    sorted_medals = sorted(medal_count.items(), key=lambda x: x[1], reverse=True) #Creates a list
    return sorted_medals[0][0]


def country_with_most_gold_medals(min_year, max_year):
    """Returns which country won the most gold medals between `min_year` and `max_year`"""
    pass  # YOUR CODE HERE

def top_three_women_in_five_thousand_meters():
    """Returns the three women with the most 5000 meters medals(gold/silver/bronze)"""
    pass  # YOUR CODE HERE

if __name__ == "__main__":
    print(most_decorated_athlete_ever())
