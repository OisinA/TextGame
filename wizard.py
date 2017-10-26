from charclass import CharClass
from enemy import Enemy
import random

class Wizard(CharClass):

  def __init__(self):
    super().__init__("Wizard")

  spell_list = ["Fireball", "Multishot"]

  def attack(self, enemy):
    terminate = False
    spell = ""
    print("Available spells: ")
    for s in self.spell_list:
        print(s, end=" ")
    print()
    while not terminate:
        print("Which spell would you like to use?")
        spell = input("> ")
        for s in self.spell_list:
            if s.lower() == spell.lower():
                terminate = True
                break;
    self.parse_spell(spell.lower(), enemy)

  def parse_spell(self, spell, enemy):
      if spell == "fireball":
          self.fireball(enemy)
      elif spell == "multishot":
          self.multishot(enemy)

  def fireball(self, enemy):
      damage = random.randint(1, 7)
      enemy.damage(damage)
      print("You damaged the %s using your fireball for %d damage." % (enemy.get_name(), damage))

  def multishot(self, enemy):
      amount = random.randint(1, 4)
      for x in range(amount):
          enemy.damage(2)
      print("You damaged the %s for %d damage, %d times." % (enemy.get_name(), amount * 2, amount))
