def navigate(robot, env, target_x, target_y):
  print(
      f"Navigating from {robot.position()} to target ({target_x}, {target_y})...")   
   
  

  current_x, current_y = robot.x, robot.y

  # Simple pathfinding simulation step
  while (current_x, current_y) != (target_x, target_y):
    # Move along X axis first
    if current_x < target_x:
      next_pos = (current_x + 1, current_y)
    elif current_x > target_x:
      next_pos = (current_x - 1, current_y)
    # Then move along Y axis
    elif current_y < target_y:
      next_pos = (current_x, current_y + 1)
    elif current_y > target_y:
      next_pos = (current_x, current_y - 1)
    else:
      break

    # Check for obstacles
    if env.blocked(next_pos[0], next_pos[1]):
      robot.avoided += 1
      print(f"Obstacle detected at {next_pos}, finding alternative...")
      # try moving sideways
      next_pos = (current_x, current_y + 1)
      if env.blocked(next_pos[0], next_pos[1]):
        return False

    current_x, current_y = next_pos
    robot.move(current_x, current_y)

    if robot.battery <= 0:
      print("Battery depleted!")
      return False

  return True
 