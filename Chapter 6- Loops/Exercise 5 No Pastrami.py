# -*- coding: utf-8 -*-
"""Exercise 5 No Pastrami

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vN3lxcXD7zjo1k6sbV8BZ7_R2hwr9oK0
"""

sandwich_orders = [
    'pastrami', 'shawarma', 'cheese', 'pastrami',
    'turkey', 'paratha', 'pastrami'] #list of sandwiches which it has 3 times 'pastrami'
finished_sandwiches = []

print("I'm sorry, we dont have pastrami today.") #deli is out of stock for pastrami
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami') #for removing pastrami in the list

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")