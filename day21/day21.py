from file_reader import get_file_entries
import re
from collections import defaultdict, deque, OrderedDict

def sub1():
    foods = get_file_entries('day21/input.txt')
    allergens_d = {}
    all_ingredients = []
    for food in foods:
        ingredients, allergens = food.split(' (contains ')
        allergens = allergens.replace(')', '').split(', ')
        ingredients = ingredients.split(' ')
        all_ingredients.extend(ingredients)
        for allergen in allergens:
            if allergen in allergens_d.keys():
                allergens_d[allergen] &= set(ingredients)
            else:
                allergens_d[allergen] = set(ingredients)
    
    # reduce
    while not all([len(x) == 1 for x in allergens_d.values()]):
        for allergen, ingredients in allergens_d.items():
            if len(ingredients) == 1:
                for other_allergen, other_ingredients in allergens_d.items():
                    if other_allergen == allergen:
                        continue
                    other_ingredients -= ingredients
    
    unclean_ingredients = [list(x)[0] for x in allergens_d.values()]
    clean_ingredients = list(set(all_ingredients) - set(unclean_ingredients))
    counter = 0
    for ingredient in all_ingredients:
        if ingredient in clean_ingredients:
            counter += 1
    print(counter)

def sub2():
    foods = get_file_entries('day21/input.txt')
    allergens_d = {}
    all_ingredients = []
    for food in foods:
        ingredients, allergens = food.split(' (contains ')
        allergens = allergens.replace(')', '').split(', ')
        ingredients = ingredients.split(' ')
        all_ingredients.extend(ingredients)
        for allergen in allergens:
            if allergen in allergens_d.keys():
                allergens_d[allergen] &= set(ingredients)
            else:
                allergens_d[allergen] = set(ingredients)
    
    # reduce
    while not all([len(x) == 1 for x in allergens_d.values()]):
        for allergen, ingredients in allergens_d.items():
            if len(ingredients) == 1:
                for other_allergen, other_ingredients in allergens_d.items():
                    if other_allergen == allergen:
                        continue
                    other_ingredients -= ingredients
    
    s = sorted(list(allergens_d.keys()))
    print(','.join([list(allergens_d[x])[0] for x in s]))