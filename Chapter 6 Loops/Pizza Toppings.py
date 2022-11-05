# -*- coding: utf-8 -*-
"""Exercise 1 Pizza Toppings.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m20eU7mPgFnlCg9ZesNHHZG-UWf1l6vE
"""

#ask for any topping in their pizza
prompt = "\nAny topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True: #while utilized to repeatedly run over an unit of code if the test expression (condition) is true.
    topping = input(prompt)
    if topping != 'quit':
        print("  I'll add " + topping + " to your pizza.")
    else: #else is includes the section of code that runs if the conditional expression in the if statement evaluates to 0 or a FALSE value.
        break #a loop control statement