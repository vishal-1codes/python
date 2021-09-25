#Here animal("name") store in def _init_(name)
class Animal(object):
      def __init__(self, name):
          self.name = name
    
zebra = Animal("Jeffrey")

print(zebra.name)