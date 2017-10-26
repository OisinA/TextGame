from charclass import CharClass
from enemy import Enemy
import random

class Wizard(CharClass):
  
  def __init__(self):
    super().__init__("Wizard")
    
  def attack(self, enemy):
    damage = random.randint(1, 7)
    enemy.damage(damage)
    print("You damaged the %s using your fireball for %d damage." % (enemy.get_name(), damage))