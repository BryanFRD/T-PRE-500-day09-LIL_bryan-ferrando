import sys
import random
import unicodedata
from os.path import exists
from tkinter import *

word_list: list = None
word: str = "" 
guess: list = []
high_score: int = -1

def generate_word():
  w = word_list[random.randint(0, len(word_list))]
  return normalize(w)

def normalize(str):
  return "".join(c for c in unicodedata.normalize("NFD", str) if unicodedata.category(c) != "Mn").upper()

if len(sys.argv[1:]) == 0 or not exists(sys.argv[1]):
  print("You must include a .txt file")
  exit()
    
f = open(sys.argv[1])
word_list = f.read().split(", ")
f.close()

if not exists("high-score.txt"):
  hsf = open("high-score.txt", 'w+')
else:
  hsf = open("high-score.txt", 'r+')

hss = hsf.read()
if hss.isdigit():
  high_score = int(hss)
  
hsf.close()

def check_highscore():
  global high_score
  if high_score == -1 or high_score > len(guess):
    high_score = len(guess)
    hsf = open("high-score.txt", 'w')
    hsf.write(str(high_score))
    hsf.close()

root = Tk()
root.title("Hangman GUI")
root.geometry("650x400")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.score = -1
root.highscore = high_score
root.check_highscore = check_highscore
root.new_highscore = False

from PlayFrame import PlayFrame
from GameFrame import GameFrame

game_frame = GameFrame(root)
game_frame.grid(row=0, column=0, sticky=NSEW)
play_frame = PlayFrame(root)
play_frame.grid(row=0, column=0, sticky=NSEW)

def switch(name = ""):
  if name == "game":
    game_frame.tkraise()
    game_frame.execute(generate_word())
  else:
    play_frame.tkraise()
    play_frame.execute()

root.switch = switch 

root.mainloop()