from tkinter import *

class GameFrame(Frame):
  
  parent = None
  guess = []
  word = ""
  score = None
  dev_label = None
  char_list_label = []
  buttons = []
  
  def __init__(self, parent):
    super().__init__(parent)
    self.parent = parent
    label = Label(self, text="Hangman")
    label.grid(row=0, column=0, columnspan=5)
    self.score = Label(self, text="Score: 0")
    self.score.grid(row=0, column=10, columnspan=2)
    
    for i in range(26):
      letter = chr(ord('A') + i)
      self.buttons.append(Button(self, text=letter, command=lambda l=letter: self.guess_word(l)))
      self.buttons[i].grid(row=int(2 + i / 10), column=int(i % 10))
    
    self.dev_label = Label(self, text="")
    self.dev_label.grid(row=5, column=0, columnspan=9)
    
  def execute(self, word):
    self.guess = []
    self.word = word
    
    self.char_list_label = []
    for i in range(len(word)):
      cl = Label(self, text="_")
      cl.grid(row=1, column=i, columnspan=10, padx=10)
      self.char_list_label.append(cl)
    
    self.dev_label.configure(text=(word if self.parent.dev else ""))
  
  def guess_word(self, str):
    self.guess.append(str)
    self.refresh()
    
  
  def refresh(self):
    ch = ([c if c in self.guess else "_" for c in self.word])
    
    if "_" not in ch:
      self.parent.score = len(self.guess)
      if self.parent.highscore > len(self.guess):
        self.parent.highscore = len(self.guess)
        self.parent.new_highscore = True 
      self.parent.switch()
      return
    
    for i in range(len(self.word)):
      self.char_list_label[i].configure(text=ch[i])
      self.char_list_label[i].update()
    
    self.score.configure(text=f"Score: {len(self.guess)}")