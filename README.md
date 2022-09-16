# Python Hangman 👨‍💼

*Day 7 of 100 days of code* 🐍

**View and run my code here ---->** https://replit.com/@PythonWrangler/pythonhangman?v=1

### Description

This is the hangman game created in Python and run from the command line. 
The app makes use of the time, os and random module. 

A text list of words is read in and stored in a list. 
The random module is used to create a random integer and index this list and then 
store the word in a variable. 

The user will be allowed to make guesses for all letters. 
.lower() is called on the given input to ensure capitalisation is consistent against the 
random word. 
Players are granted six lives and their lives deplete for incorrect guesses. 
If a guess is correct the program replaces all instances of that letter in the word
and return a print statenment of how many times the letter appears in the word as well as
an updated view of the random word with the guesses filled in. 

### What I learnt: 🧑‍💻
- using the os module to clear the screen
- while loops
- reading in text files
- using the random module to generate a random integer
- using the time module to add delay to my program  