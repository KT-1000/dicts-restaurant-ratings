# your code goes here
from sys import argv

restaurant_data = argv[1]

def get_restaurant_ratings(file_name):

    restaurant_ratings = {}
    restaurant_name_input = raw_input('Give me a restaurant name: ')
    restaurant_rating_input = raw_input('What\'s the rating? ')
    restaurant_ratings[restaurant_name_input] = restaurant_rating_input

    with open(file_name) as in_file:

        for line in in_file:
            name, rating = line.strip().split(':')
            restaurant_ratings[name] = rating

    for name in sorted(restaurant_ratings):
        print name + " is rated at " + str(restaurant_ratings[name]) + "."


get_restaurant_ratings(restaurant_data)