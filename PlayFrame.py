from tkinter import *

class PlayFrame(Frame):
  
  parent = None
  hs = None
  score_label = None
  highscore_label = None
  
  def __init__(self, parent):
    super().__init__(parent)
    self.parent = parent
    title = Label(self, text="Would you want to play")
    title.grid(row=0, column=0, columnspan=9)
    self.hs = Label(self, text=f"Highscore: {parent.highscore}")
    self.hs.grid(row=1, column=0, columnspan=9)
    
    self.score_label = Label(self)
    self.score_label.grid(row=2, column=0, columnspan=9)
    self.highscore_label = Label(self)
    self.highscore_label.grid(row=3, column=0, columnspan=9)
    
    def play_command(asDev = False):
      parent.dev = asDev
      parent.switch("game")
    
    play = Button(self, text="Play", command=lambda: play_command(False))
    play.grid(row=4, column=0)
    dev = Button(self, text="Play as dev", command=lambda: play_command(True))
    dev.grid(row=4, column=1)
    quit = Button(self, text="Quit", command=lambda: exit(0))
    quit.grid(row=4, column=2)
  
  def execute(self):
    if not self.parent.score == -1:
      self.score_label.configure(text=f"Score: {self.parent.score}")
    
    if self.parent.new_highscore:
      self.highscore_label.configure(text="You've set a new highscore !")
    
    self.parent.new_highscore = False
    
    self.hs.configure(text=f"Highscore: {self.parent.highscore}")