# -*- coding: utf-8 -*-
"""Exercise 4 Rivers.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ap8BCLojhIjktB6rdajmByF1W4H8HnFJ
"""

#think about countries that has famous rivers
rivers = {'Egypt': 'Nile', 'Brazil': 'Amazon', 'Russia': 'Yenisei'}

for river, country in rivers.items():
    print("The " + river.title() + " flows through " + country.title() + ".")

print("\nThe following countries are included in this data set:") #define the countries
for river in rivers.keys():
    print("- " + river.title())

print("\nThe following rivers are included in this data set:") #define the rivers
for country in rivers.values():
    print("- " + country.title())