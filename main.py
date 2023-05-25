# Watto needs a new system for organizing his inventory of podracers. 
# Help him do this by implementing an Object Oriented solution according to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.

class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

# Define a repair() method that will update the condition of the podracer to "repaired".

def repair(self):
  self.condition = "repaired"

# Define new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.

class AnakinsPod:
  def __init__(self, max_speed, condition, price):
    super.init(self, max_speed, condition, price)

    def boost(self):
         self.max_speed *= 2

# Define another class that inherits Podracer and call this one SebulbasPod. 
# This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".

class SebulbasPod:
    def __init__(self, max_speed, condition, price):
      super.init(self, max_speed, condition, price)

    def flame_jet(self):
      self.condition = "trashed"
   
# How does this solution ensure data immutability?
    # By using self and the same values

# Is this solution a pure function? Why or why not?
    # Yes, this is a pure function, it has the same input params

# Is this solution a higher order function? Why or why not?
    # Yes this is a higer order function because Podracer and other functions return a result

# Would it have been easier to solve this problem using a different programming style?
    # This way seems like the simplest form to write and understand, the other styles dont seem to fit 

# Why in particular is functional programming a helpful paradigm when solving this problem?
    # It has variables that are passed as arguments and return from other functions

#How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
# Encapsulation is not used due to I'm not hiding information from one function to another
# Abstraction is not used due to not hiding functions
# Inheritance is used due to the parent child relationship of classes using the same params
# Polymorphism is used because of sharing behaviors and allowing custom overrides

# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
    # If using a different coding style, their would have been a lot more indepth code to write

# How in particular did Object Oriented Programming assist in the solving of this problem
    # OOP helped by using inheritance and polymorphism, being able to take the parent and make children classes to follow the parent but still show as a result with small easy code to write
