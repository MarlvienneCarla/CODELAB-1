# -*- coding: utf-8 -*-
"""Exercise 4 Deli.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eU9wEPao4xW4guGN5972VbphHbdDayDU
"""

sandwich_orders = ['shawarma', 'cheese', 'paratha', 'turkey'] #make a list for sandwich orders
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.") #make a statement for like doing the sandwich
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.") #list of finished orders