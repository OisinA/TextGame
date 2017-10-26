import random
from charclass import CharClass

'''
This class stores information about the player. It has a function for each of the player's actions.
'''
class Player():
  
  name = ""
  health = 15
  dodge = False
  charclass = CharClass("None")
  
  '''
  Class constructor, requires name (string) and health (integer) parameter.
  '''
  def __init__(self, name, health, charclass):
    self.name = name
    self.health = health
    self.charclass = charclass
  
  '''
  This function returns the name of the player.
  '''
  def get_name(self):
    return self.name
  
  '''
  This function returns the health of the player.
  '''
  def get_health(self):
    return self.health
  
  '''
  This function is called when the player takes damage, requiring the damage (integer) parameter.
  '''
  def damage(self, damage):
    damage_modifier = self.charclass.get_damage_modifier()
    final_damage = int(damage * self.charclass.get_damage_modifier())
    if not damage_modifier == 1:
      print("You are taking %d%% damage." % (damage_modifier * 100))
      print("The enemy hit for %d, but you instead took %d damage." % (damage, final_damage))
    else:
      if self.dodge:
        outcome = random.randint(1, 3)
        if outcome == 1:
          print("You successfully dodged the attack!")
          return
        else:
          print("You tried to dodge the attack, but failed.")
      print("You took %d damage!" % final_damage)
    self.health -= final_damage
    
  '''
  This is called when a player goes to attack an enemy. It requires the enemy (Enemy) and damage (Integer) parameter.
  '''
  def attack(self, enemy):
    self.charclass.attack(enemy)

  '''
  This function allows the player to attempt to dodge the enemy's next attack.
  '''
  def perform_dodge(self):
    self.dodge = True
    
  '''
  This function resets the player's action, setting dodge to false.
  '''
  def reset_turn(self):
    self.dodge = False
    
  '''
  This function allows the user to attempt to flee, but killing them instead.
  '''
  def flee(self):
    print("You attempt to flee, but are struck down as you run away.")
    self.health = 0
    
    
  '''
  This function parses the user's input and converts it to an action. Takes in the action (String) parameter.
  '''
  def perform_action(self, action, enemy):
    if action == "attack":
      self.attack(enemy)
    elif action == "dodge":
      self.perform_dodge()
    elif action == "flee":
      self.flee()
      return True
    return False