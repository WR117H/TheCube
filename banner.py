from colorama import Fore
import shutil
from time import sleep
import time
import keyboard
import os

CHOICE=0
def CLEAR():
    os.system("clear||cls")
def DELAY(intj):
    sleep(intj)


def GREEN():

   color=Fore.LIGHTGREEN_EX
   print(color)
ASCII="""
  ________         ______      __       
 /_  __/ /_  ___  / ____/_  __/ /_  ___ 
  / / / __ \/ _ \/ /   / / / / __ \/ _ \\
 / / / / / /  __/ /___/ /_/ / /_/ /  __/
/_/ /_/ /_/\___/\____/\__,_/_.___/\___/
"""

ASCII1="""⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢴⣤⣄⠀⠀⠀⠀⠀⢀⣤⣶⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀
⢴⣾⣿⣿⣿⣏⣉⣉⣉⣛⣛⣻⣿⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠙⢷⠀⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣾⣿⣛⣛⣋⣉⣉⣉⣿⣿⣿⣿⣶⠄
⠀⠙⢿⣿⣿⣿⡁⠀⠀⣉⡿⠋⠉⠉⠙⠛⠻⢿⣦⣄⠀⠀⠀⠀⠘⣇⠀⢀⡟⠀⠀⠀⠀⢀⣤⣾⠿⠛⠋⠉⠉⠉⠻⣏⡉⠀⠈⣹⣿⣿⣿⠟⠁⠀
⠀⠀⠀⠙⣿⣿⣟⠉⠉⣙⡇⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣦⡀⠀⠀⢹⠀⣸⠃⠀⠀⣠⣾⠟⠋⠀⠀⠀⠀⠀⠀⠀⢀⣿⡉⠉⠹⣿⣿⡟⠉⠀⠀⠀
⠀⠀⠀⠀⠈⢿⣿⣟⠉⢉⣿⣦⣄⣀⣀⠀⠀⠀⠀⠀⠀⠙⢿⣦⡀⠸⡇⡿⠀⣠⣾⠟⠁⠀⠀⠀⠀⠀⢀⣀⣀⣤⣾⣍⠉⠙⣿⣿⡯⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠸⣿⣿⣿⠉⠀⠀⣀⣨⡟⠛⠛⠒⠒⠤⢄⣀⠀⠙⢿⣆⣷⣧⣾⠟⠁⠀⣀⠤⠄⠒⠚⠛⠛⣯⣀⡀⠀⠉⢹⣿⣿⡿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⡟⠉⣀⡤⢷⡦⠄⠀⠀⠀⠀⠈⠙⠢⣌⣻⣿⣿⢋⠤⠚⠉⠀⠀⠀⠀⠀⠠⣶⠷⣄⡈⠙⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⠿⣿⣿⣿⣁⡤⠾⣷⣤⣴⠶⢶⣒⡻⠿⠿⢛⣿⣿⣿⣟⠛⠽⠿⢓⣲⠶⢶⣦⣴⡟⠦⣄⣹⣿⣿⡿⠟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⣿⣿⣿⢛⣉⠥⠒⠉⠁⠀⣀⠔⢈⠔⣽⣿⣿⡝⢌⠒⢄⡀⠀⠉⠑⠢⢍⣙⢻⣿⣿⡟⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⠋⠀⠀⠀⢀⡤⠊⠀⡴⠋⣼⡟⣿⡟⢿⡄⠳⡄⠈⠢⣀⠀⠀⠀⠈⢻⣷⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣯⢽⣀⠀⣀⣴⡏⠀⢀⡞⠁⣸⡿⠀⠉⠀⠘⣿⡀⠙⣆⠀⠘⣷⣄⡀⢀⡸⢯⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⣿⣿⡶⠋⡿⠋⣽⠷⣶⡟⠀⢰⣿⠃⠀⠀⠀⠀⢹⣧⠀⠘⣷⡖⢿⡍⠻⡏⠳⣶⣿⡟⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣷⡞⠀⢠⡇⢰⡟⠀⠀⣾⡏⠀⠀⠀⠀⠀⠈⣿⡆⠀⠘⣧⠀⣷⠀⠹⣶⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣶⡟⠙⣿⡀⠀⣰⡿⠀⠀⠀⠀⠀⠀⠀⠸⣷⡀⠀⣹⣟⠙⣷⣾⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⢿⣿⣿⣿⡿⠿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⠿⠿⣿⣿⣿⣿⠟⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
def banner():
    os.system("clear||cls")
    print(ASCII)

def middle(ASCII):
    os.system('clear||cls')
    console_width = shutil.get_terminal_size().columns

    # Split ASCII art into lines
    lines = ASCII.strip().split('\n')

    # Calculate maximum line width
    max_line_width = max(len(line) for line in lines)

    # Print ASCII art with centered lines
    for line in lines:
        indentation = (console_width - len(line)) // 2
        print(' ' * indentation + line)
def butterfly():
    middle(ASCII1)
def STRING(text):
    

    text = text
    for char in text:
        print(char, end='', flush=True)  # Print the character without a newline
        DELAY(0.1)
    print()
    
def blink_input(prompt):
    
    text = prompt
    if CHOICE > 0:
        print()
    for char in text:
        print(char, end='', flush=True)  # Print the character without a newline
        DELAY(0.1)
    while True:
        # Wait for key press
        key = input()

        if key == '1':
            choice = '1'
            DELAY(0.4)
            return choice
            break
        elif key == '2':
            choice = '2'
            
            DELAY(0.4)
            return choice
            break
        else:
            print("Invalid choice. Please try again.")

def start_game():
    global CHOICE
    STRING("Once upon a time...")

    prompt = "You find yourself in a mysterious forest. What do you do? (1. Explore deeper, 2. Follow a path): "
    choice = blink_input(prompt)
    CHOICE+=1
    

    if choice == "1":
        explore_deeper()
    elif choice == "2":
        follow_path()
    else:
        STRING("Invalid choice. Please try again.")
        start_game()
def explore_deeper():
    STRING("You decide to explore deeper into the forest.")
    STRING("You stumble upon an old cabin.")
    prompt="What do you do? (1. Enter the cabin, 2. Keep exploring): "
    choice = blink_input(prompt)

    if choice == "1":
        enter_cabin()
    elif choice == "2":
        keep_exploring()
    else:
        STRING("Invalid choice. Please try again.")
        explore_deeper()


def enter_cabin():
    STRING("You cautiously enter the cabin.")
    STRING("Inside, you find a table with three items: a key, a map, and a mysterious book.")
    prompt = "What do you take with you? (1. Key, 2. Map, 3. Book): "
    choice = blink_input(prompt) 
    

    if choice == "1":
        STRING("You take the key and leave the cabin.")
        STRING("As you continue your journey, you encounter a locked door.")
        prompt = "What do you do? (1. Use the key, 2. Find another way): "
        choice = blink_input(prompt)
        if choice == "1":
            STRING("You unlock the door and find a hidden treasure!")
            game_over()
        elif choice == "2":
            STRING("You search for another way but get lost in the forest.")
            STRING("Unable to find your way back, you give up.")
            game_over()
        else:
            STRING("Invalid choice. Please try again.")
            enter_cabin()

    elif choice == "2":
        STRING("You take the map and leave the cabin.")
        STRING("You follow the map and discover a hidden treasure!")
        game_over()

    elif choice == "3":
        STRING("You take the mysterious book and leave the cabin.")
        STRING("The book contains ancient spells that you cannot decipher.")
        STRING("You continue your journey without any significant discoveries.")
        game_over()

    else:
        STRING("Invalid choice. Please try again.")
        enter_cabin()


def keep_exploring():
    STRING("You decide to keep exploring the forest.")
    STRING("You encounter a talking squirrel who offers you a riddle.")
    prompt = "Do you accept the riddle challenge? (1. Yes, 2. No): "
    choice = blink_input(prompt)

    if choice == "1":
        STRING("The squirrel asks: 'I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?'")
        prompt = "What is your answer? "

        answer = blink_input(prompt)

        if answer.lower() == "echo":
            STRING("Congratulations! You answered correctly!")
            STRING("The squirrel leads you to a hidden treasure!")
            game_over()
        else:
            STRING("Oops! That's incorrect. The squirrel disappears, leaving you disappointed.")
            game_over()

    elif choice == "2":
        STRING("You politely decline the squirrel's offer and continue exploring.")
        STRING("You eventually find a hidden treasure!")
        game_over()

    else:
        STRING("Invalid choice. Please try again.")
        keep_exploring()


def follow_path():
    STRING("You decide to follow a path through the forest.")
    STRING("The path leads you to a magical waterfall.")
    prompt = "What do you do? (1. Dive into the water, 2. Explore around the waterfall): "
    choice = blink_input(prompt)
    if choice == "1":
        STRING("You dive into the water and discover a hidden underwater cave.")
        STRING("Inside the cave, you find a chest containing a priceless artifact!")
        game_over()

    elif choice == "2":
        STRING("You explore around the waterfall and find a hidden pathway.")
        STRING("The pathway leads you to a secret garden with beautiful flowers.")
        STRING("You enjoy the serenity of the garden and continue your journey.")
        game_over()

    else:
        STRING("Invalid choice. Please try again.")
        follow_path()


def game_over():
    STRING("Game over. Thank you for playing!")