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
    #Step 1- Extract the country with the most gold medals from MEDALS_FILEPATH
    medal_count = {}
    with open(MEDALS_FILEPATH, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if int(row["Year"]) > min_year and int(row["Year"]) < max_year:
                if row["Country"] in medal_count.keys():
                    medal_count[row["Country"]] += 1
                else:
                    medal_count[row["Country"]] = 1

    sorted_medals = sorted(medal_count.items(),
                           key=lambda x: x[1],
                           reverse=True)  #Creates a list
    top_country = sorted_medals[0][0]
    #Step 2- Use COUNTRIES_FILEPATH to return the name of that country
    country_list = {}
    with open(COUNTRIES_FILEPATH, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            country_list[row["Code"]] = row["Country"]

    return country_list[top_country]



def top_three_women_in_five_thousand_meters():
    """Returns the three women with the most 5000 meters medals(gold/silver/bronze)"""
    pass  # YOUR CODE HERE

if __name__ == "__main__":
    print(country_with_most_gold_medals(1980,2000))
