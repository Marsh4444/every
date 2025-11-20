from random import randint



class Die:

    def __init__(self, sides = randint(1,10)):
        """A die with 6 sides"""
        self.sides = sides

    def roll_die(self):
        """prints a random number between 1 and the no of sides the die has"""
        roll = f"This is the result of the die: {self.sides}"
        return roll

  #  def roll_tentimes(self, time = 0, times= 11):
  #      """rolls the die 10x"""
  #      self.time = time
  #      self.times = times
  #      while self.time < self.times:
  #          print(f"This is the number on the die: {self.sides}\n" )

   #         self.time += 1

roll_1 = Die()
i = 0
p = 11

while i < p:
    print(roll_1.roll_die())
    i += 1
    
    
