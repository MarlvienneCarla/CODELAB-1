# -*- coding: utf-8 -*-
"""Exercise 2 Alien Colors #2.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dQA0_AMK_Td0Wsuio7Xgb5-gUlGmjPu5
"""

#the colors green, yellow and red
#ask for a color
alien_color = ['green', 'yellow', 'red']
print('Choose an alien color: ')
alien_color=str(input())
if alien_color is 'green' :
  print('the player just earned 5 points')
else:
  print('The player just earned 10 points')