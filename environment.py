class Environment:

  def __init__(self):
    self.obstacles = []

  def add_obstacle(self, x, y):
    if (x, y) not in self.obstacles:
      self.obstacles.append((x, y))

  def blocked(self, x, y):
    return (x, y) in self.obstacles