class Robot:

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.steps = 0
    self.battery = 100
    self.avoided = 0
    self.path = [(x, y)]

  def position(self):
    return (self.x, self.y)

  def move(self, x, y):
    self.x = x
    self.y = y
    self.path.append((x, y))
    self.steps += 1
    if self.battery > 0:
      self.battery -= 5
      
