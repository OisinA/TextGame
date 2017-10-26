from enemy import Enemy

class CharClass:
  
  name = ""
  
  def __init__(self, name):
    self.name = name
    
  def attack(self, enemy):
    enemy.damage(5)
    print("You damaged the enemy for 5 damage")
    
  def get_damage_modifier(self):
    return 1
  
  def get_name(self):
    return self.name