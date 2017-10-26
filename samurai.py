from charclass import CharClass
from enemy import Enemy
import random

class Samurai(CharClass):

  def __init__(self):
    super().__init__("Samurai")

  def attack(self, enemy):
    damage = random.randint(1, 6)
    enemy.damage(damage)
    print("You damaged the %s using your sword for %d damage." % (enemy.get_name(), damage))

  def get_damage_modifier(self):
    return 0.8
