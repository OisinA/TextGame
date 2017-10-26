import random

'''
This class stores information about the enemy. It has a difficulty rating that controls the health and damage of the enemy.
'''
class Enemy():
  
  name = ""
  health = 0
  difficulty = 1
  
  '''
  Class constructor, takes the name (String) and difficulty (Integer) parameters. Difficulty sets the health and damage of the enemy.
  '''
  def __init__(self, name, difficulty):
    self.name = name
    self.health = 20 * difficulty
    self.difficulty = difficulty
    
  '''
  This function returns the name of the enemy.
  '''
  def get_name(self):
    return self.name
  
  '''
  This function returns the health of the enemy.
  '''
  def get_health(self):
    return self.health
  
  '''
  This function takes health away from the enemy, taking the damage (Integer) parameter.
  '''
  def damage(self, damage):
    self.health -= damage
    
  '''
  This function returns the difficulty of the enemy.
  '''
  def get_difficulty():
    return self.difficulty
    
  '''
  This function allows the enemy to attack the player, taking player (Player) as a parameter.
  '''
  def attack(self, player):
    print("The %s goes for an attack." % self.name)
    player.damage(random.randint(1, 5) * self.difficulty)