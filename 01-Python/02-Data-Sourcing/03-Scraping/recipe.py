# pylint: disable=missing-docstring,line-too-long
import sys
from os import path
import requests
from bs4 import BeautifulSoup
import csv

def parse(html):
    ''' return a list of dict {name, difficulty, prep_time} '''
    # response = requests.get(html)
    soup = BeautifulSoup(html, "html.parser")
    recipes = []
    for recipe in soup.find_all("div", class_="p-2 recipe-details"):
        name = recipe.find(
            "p",
            class_=
            "text-dark text-truncate w-100 font-weight-bold mb-0 recipe-name").string.strip()
        difficulty = recipe.find("span", class_="recipe-difficulty").string.strip()
        prep_time = recipe.find("span", class_="recipe-cooktime").string.strip()

        recipes.append({'name': name,
                        'difficulty': difficulty,
                        'prep_time':  prep_time})
    return recipes

def write_csv(ingredient, recipes):
    ''' dump recipes to a CSV file `recipes/INGREDIENT.csv` '''
    with open(f'recipes/{ingredient}.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = recipes[0].keys())
        writer.writeheader()
        for recipe in recipes:
            writer.writerow(recipe)

def scrape_from_internet(ingredient, start=1):
    ''' Use `requests` to get the HTML page of search results for given ingredients. '''
    url = f"https://recipes.lewagon.com/"
    response = requests.get(url,
                            params={
                                'search[query]': ingredient,
                                'page': start
                            })
    if response.history:
       return None
    else:
        return response.content

def scrape_from_file(ingredient):
    file = f"pages/{ingredient}.html"
    if path.exists(file):
        return open(file)
    print("Please, run the following command first:")
    print(f'curl "https://recipes.lewagon.com/?search[query]={ingredient}" > pages/{ingredient}.html')
    sys.exit(1)

def main():
    if len(sys.argv) > 1:
        ingredient = sys.argv[1]
        # TODO: Replace scrape_from_file with scrape_from_internet and implement pagination (more than 2 pages needed

        start = 1
        recipes = []
        while start <6:
            if scrape_from_internet(ingredient,start = start):
                recipes += parse(scrape_from_internet(ingredient,start = start))
                print("Page ", start)
                start += 1
            else:
                break
        write_csv(ingredient, recipes)

    else:
        print('Usage: python recipe.py INGREDIENT')
        sys.exit(0)

if __name__ == '__main__':
    main()
