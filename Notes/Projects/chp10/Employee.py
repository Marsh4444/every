class Employee:
    """Takes name and annual salry of a person"""

    def __init__(self, first, last, annual):
        """The annual salary of the person"""
        self.first = first
        self.last = last
        self.annual = annual
        self.new = ''

    def give_raise(self, add = 5000):
        self.add = add
        new_annual = self.annual + self.add
        new_ann = f"{self.first} {self.last} has a payment of {new_annual}"
        new_ann = new_ann.title()
        self.new = new_ann
        return self.new
        #print(self.new.append(new_ann))


employee_1 = Employee('marsh','melo',10000)
print(employee_1.give_raise())
