
#!/usr/bin/py
"""This is a program that gives the user a word which is jungled up and tells the user to find the correct word"""
#I also want it to take some words from another file and ask the user to answer the questions. It should  ask the user 10 words and give them a total score. If the user is having a hard
#time, he can request for a hint by pressing h.

"""Now I want to expand this game so that it fetches a word from an online dictionary, shows it to the player, and, if the player wants a hint, the definition of the word from the online
dictionary is fetched and showd to him"""

import hintfile #The file that contains definitions of words
from hintfile import Definition
import random

name = 'derrick'
newname = []
for letter in name:
    newname.append(letter)
random.shuffle(newname)
print(newname)

answer = input("What's the right word? ")
if answer == name or answer == name.title():
    print("You're right\n")
else:
    print("Wrong, try again!\n")


listwords = []
with open('hardtexts.txt','r') as file:
    try:
        words = file.readlines()    
        for word in words:
            listwords.append(word.rstrip()) #place the words in a list called listwords      
    except EOFError:
        pass       

n = 0
allword = [] #list to insert characters of each word, so that they can be shuffled. 
while n <= 7: 
    for letter in listwords[n]:
        allword.append(letter)
    random.shuffle(allword)
    print(allword)
    answer = input("What's the correct word?: (Type h for a hint) ") 

    if answer == listwords[n] or answer == listwords[n].lower():
        print("You're right\n\n")

    elif answer == 'h':
        print(Definition(listwords[n]))
        answerafterhint = input("What is the answer now?: ")
        if answerafterhint == listwords[n] or answerafterhint == listwords[n].lower():
            print("You're right\n")
        else:
            print("You're wrong\n.The answer is " + listwords[n] + "\n")
         
    else:
        print("You're wrong")
        print("Answer is " + listwords[n] + " .\n")
    allword.clear()  #This list method erases all elements in the list
    n = n + 1
