class Calculator:
  
  def add(x, y):
    return x + y

  def subtract(x, y):
    return x - y

  def multiply(x, y):
    return x * y

  def divide(x, y):
    if y == 0:
      raise ValueError('Undefined')
    return x / y

  def powerof(x, y):
    if y > 0:
      count = 1
      while y > 0:
        count = count * x
        y -= 1
      return count
    elif y < 0:
      y = -y
      count = 1
      while y > 0:
        count = count * 1/x
        y-=1
      return count
    return 1
  