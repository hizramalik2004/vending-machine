# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 20:34:14 2024

@author: DELL
"""

def vending(drinks, snacks):  # Creates a function named 'vending'
    print("VENDING MACHINE")
    print("Which category would you like?")
    print("Press")
    print("1 for drinks")
    print("2 for snacks")
    cat = int(input("Enter the category: "))

    if cat == 1:  # Drinks
        print("Here is a list of drinks")
        for i in range(len(drinks)):
            print(drinks[i][0], '', drinks[i][1], '', drinks[i][2], '_', drinks[i][3])
        print("Enter the code for the item of your choice")
        drinkcode = input()
        for j in range(len(drinks)):
            if drinks[j][0] == drinkcode:
                print("The price is:", drinks[j][2])
                drinkspaid = int(input("Please insert money"))
                if drinkspaid >= drinks[j][2]:
                    print("Thank you for purchasing")
                    print("Here is your change:", drinkspaid - drinks[j][2])
                    drinks[j][3] -= 1
                else:
                    print("Can't accept because it is not enough, please try again")
                if drinks[j][3] == 0:
                    print("Sorry, item is out of stock")
                break
    elif cat == 2:  # Snacks
        print("Here is a list of snacks")
        for i in range(len(snacks)):
            print(snacks[i][0], '', snacks[i][1], '', snacks[i][2], '_', snacks[i][3])
        print("Enter the code for the item of your choice")
        snackcode = input()
        for j in range(len(snacks)):
            if snacks[j][0] == snackcode:
                print("The price is:", snacks[j][2])
                snackspaid = int(input("Please insert money"))
                if snackspaid >= snacks[j][2]:
                    print("Thank you for purchasing")
                    print("Here is your change:", snackspaid - snacks[j][2])
                    snacks[j][3] -= 1
                else:
                    print("Can't accept because it is not enough, please try again")
                if snacks[j][3] == 0:
                    print("Sorry, item is out of stock")
                break
    else:
        print("Category not found, please try again")

def ask():  # Creates a function named ask which asks the user if they want to buy something else
    print("Would you like to buy anything else? Press 'Y' for yes")
    ans = input()
    if ans == 'Y':
        vending(drinks, snacks)
    else:
       print("Thank you!")

drinks = [['1', 'cola', 4, 12], ['2', 'juice', 5, 8], ['3', 'tea', 2, 21]]  # A nested list of drinks with their codes, price, and stock
snacks = [['1', 'chips', 5, 14], ['2', 'cookies', 4, 11], ['3', 'cake', 6, 4]]  # A nested list of snacks with their codes, price, and stock

vending(drinks, snacks)  # This will start/call the function named 'vending'