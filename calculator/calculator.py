class Calculator:
  
  def add(x, y):
    return x + y

  def subtract(x, y):
    return x - y

  def multiply(x, y):
    return x * y

  def divide(x, y):
    return x / y

  def powerof(x, y):
    count = 1
    while y > 0:
      count = count * x
      y -= 1
    return count
