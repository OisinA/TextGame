import random
from player import Player
from enemy import Enemy
from wizard import Wizard
from barbarian import Barbarian

charclasses = [Wizard(), Barbarian()]

'''
This function prompts the user for their class and returns thie chosen class.
'''
def get_user_class():
  terminate = False
  charclass = ""
  while not terminate:
    print("What class would you like to play?")
    charclass = input("> ")
    for c in charclasses:
      if c.get_name().lower() == charclass.lower():
        terminate = True
        break
  return user_class(charclass.lower())
  
'''
This function converts from the user's input into their chosen class.
'''
def user_class(charclass):
  for c in charclasses:
    if c.get_name().lower() == charclass:
      return c
  
'''
Read in the player's input and convert it to their action.
'''
def read_input():
  success = False
  action = ""
  while not success:
    line_separator("=")
    print("Attack, dodge or flee?")
    user_input = input("> ")
    if user_input.lower() == "attack" or user_input.lower() == "dodge" or user_input.lower() == "flee":
      action = user_input.lower()
      success = True
  return action

'''
Main function of the game. This is called each turn.
'''
def main():
  player.reset_turn()
  terminate = False
  action = read_input()
      
  line_separator("=")
  
  terminate = player.perform_action(action, enemy)
  
  line_separator("*")
  
  if enemy.get_health() > 0:
    enemy.attack(player)
    print("Your remaining health is %d." % player.get_health())
    print("The %s has %d health remaining." % (enemy.get_name(), enemy.get_health()))
  
  if(player.get_health() <= 0):
    line_separator("=")
    print("You have died.")
    line_separator("s")
    terminate = True
  
  if(enemy.get_health() <= 0):
    print("You have killed the enemy!")
    terminate = True
    
  return terminate

  
'''
This function prints a line separator to the output.
'''
def line_separator(s):
  print(s * 22)

charclass = get_user_class() #Fetch player class.
print("You have chosen the %s class." % charclass.get_name())
player = Player("Oisin", 15, charclass) # Initiate player object.
enemy = Enemy("Zombie", 2) # Initiate enemy object.

line_separator("=")
print("You are playing as %s. You have %d health." % (player.get_name(), player.get_health()))
print("You have come across a %s, who has %d health." % (enemy.get_name(), enemy.get_health()))
terminate = False
while not terminate:
  terminate = main()
  
print("The game is over.")
line_separator("=")
