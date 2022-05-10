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