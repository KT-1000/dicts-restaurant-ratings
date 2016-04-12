# your code goes here
from sys import argv

restaurant_data = argv[1]

def get_restaurant_ratings(file_name):

    restaurant_ratings = {}

    with open(file_name) as in_file:

        for line in in_file:
            name, rating = line.strip().split(':')
            restaurant_ratings[name] = rating

    for name in sorted(restaurant_ratings):
        print name, "is rated at", restaurant_ratings[name] + "."


get_restaurant_ratings(restaurant_data)