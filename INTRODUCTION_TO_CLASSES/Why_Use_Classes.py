class Fruit(object):
      """A class that makes various tasty fruits."""
  def __init__(self, name, color, flavor, poisonous):
    self.name = name
    self.color = color
    self.flavor = flavor
    self.poisonous = poisonous

#Python is an object-oriented programming language, which means it manipulates programming constructs called objects. 
#A class is just a way of organizing and producing objects with similar attributes and methods.
  def description(self):
    print("I'm a %s %s and I taste %s.") % (self.color, self.name, self.flavor)

  def is_edible(self):
    if not self.poisonous:
      print("Yep! I'm edible.")
    else:
      print("Don't eat me! I am super poisonous.")

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()
