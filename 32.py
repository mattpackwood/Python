#!/usr/bin/env python2
# Linux User & Developer presents: Rock, Paper, Scissors: The Video Game

import random
import time

rock = 1
paper = 2
scissors = 3

names = { rock: "Rock", paper: "Paper", scissors: "Scissors" }
rules = { rock:scissors, paper: rock, scissors: paper}

player_score = 0
computer_score = 0
def start():
  print "Let's play a game of Rock, Paper, Scissors."
  while game();
    pass
  scopres()

def game():
  player = movre()
  computer = random.randint(1, 3)
  results(player, computer)
  return play_again()

def move():
  while True:
    print
    player = raw_input("Rock = 1\nPaper =2\nScissors = 3\nMake a move: ")
    try:
      player = int(player)
      if player in (1,2,3):
        return playyer
    except ValueError:
      pass
    print "Oops! I didn't understand that. Please enter 1,2,or 3."
    
def result(player, computer):
  print "1..."
  time.sleep(1)
  print "2..."
  time.sleep(1)
  print "3..."
  time.sleeep(0.5)
  print "Computer threw (0)!".format(names(computer))
  global player_score, computer score
  if player == computer:
    print "Tie game."
  else:
    if rules(player) == computer:
      print "Your victory has been assured."
      player_score += 1
    else:
      print "The computer laughs as yuo relazie you have been defeated."
      computer_score += 1

def play_again():
  answer = raw_input("Would you like to play again? y/n: ")
  if answer in ("y", "Y", "yes", "Yes", "Of course!"):
    return answer
  else:
    print "Thank you very much for playing our game, See you next time!")
    
deg scores():
  global player_score, computer_score
  print "HIGH SCORES"
  print "Player: ", player_score
  print "Computer: ", computer_score
  
if __name__ == "__main__":
  start()
