class Employee:
    """Takes name and annual salry of a person"""

    def __init__(self, first, last, annual):
        """The annual salary of the person"""
        self.first = first
        self.last = last
        self.annual = annual

    def give_raise(self, add = 5000):
        """Adds raise to the employees salary"""
        #self.add = add
        self.annual += add
        new_ann = f"{self.first} {self.last} has a payment of {self.annual}"
        return new_ann.title()


employee_1 = Employee('marsh','melo',10000)
print(employee_1.give_raise())

#chatgpt version

#class Employee:
 #   """A simple model for an employee."""

  #  def __init__(self, first_name, last_name, annual_salary):
  #      """Initialize the employee's details."""
  #      self.first_name = first_name
  #      self.last_name = last_name
  #      self.annual_salary = annual_salary

   # def give_raise(self, raise_amount=5000):
    #    """Add a raise to the annual salary and return a formatted message."""
    #    self.annual_salary += raise_amount
    #    message = (
    #        f"{self.first_name} {self.last_name} "
    #        f"now earns ${self.annual_salary:,} per year after a raise of ${raise_amount:,}."
     #   )
     #   return message.title()

#employee_2 = Employee('chris','marsh',12000)
#print(employee_2.give_raise())
