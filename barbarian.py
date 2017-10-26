from charclass import CharClass
from enemy import Enemy
import random

class Barbarian(CharClass):
  
  def __init__(self):
    super().__init__("Barbarian")
    
  def attack(self, enemy):
    damage = random.randint(1, 4)
    enemy.damage(damage)
    print("You damaged the %s using your sword for %d damage." % (enemy.get_name(), damage))

  def get_damage_modifier(self):
    return 0.5