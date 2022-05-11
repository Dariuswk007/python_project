# create a function with 6 variables
# has to add up product items
# must have sales tax
# must print a dynamic total




def sales_calc(*args):
  sum = 0
  for product in args:
    sum = sum + product
  total = 0.7 * sum
  print(f'Thank you for shopping with us. Your total is ${total}.')
  return total


sales_calc(30, 30, 20, 20, 60, 10)



class Multiples:
  def __init__(self, adder, subractor, divider, multiplier):
    self.adder = adder
    self.subractor = subractor
    self.divider = divider
    self.multiplier = multiplier

  def the_adder(self):
    return self.adder + 2

  def the_subtractor(self):
    return self.subractor - 2

  def the_divider(self):
    return self.divider / 2

  def the_multiplier(self):
    return self.multiplier * 2


first = Multiples(1, 2, 3, 4)
print(first.the_adder())
print(first.the_subtractor())
print(first.the_divider())
print(first.the_multiplier())
