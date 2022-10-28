# -*- coding: utf-8 -*-
"""Exercise 5 Pets

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GhTnKIzJ1-FRinG2JURF4EjOYYwXGU_d
"""

# Make an empty list to store the pets in.
pets = []

# Make individual pets: store each one in the list.
pet = {
    'animal type': 'Cat',
    'name': 'Rus',
    'owner': 'Yen',
    'weight': 26,
    'eats': 'rat',
}
pets.append(pet)

pet = {
    'animal type': 'Mice',
    'name': 'alvin',
    'owner': 'Clair',
    'weight': 2,
    'eats': 'corn',
}
pets.append(pet)

pet = {
    'animal type': 'Dog',
    'name': 'Kevin',
    'owner': 'Rile',
    'weight': 24,
    'eats': 'slippers',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))