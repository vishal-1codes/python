#Classes can have member variables that store information about each class object. We call them member variables since they are information that belongs to the class object.
class Car(object):
  def __init__(self,model,color,mpg):
    self.model=model
    self.color=color
    self.mpg=mpg

  condition="new"

my_car= Car("DeLorean","silver",88)

print(my_car.condition)