from environment import Environment 
from navigation import navigate
from robot import Robot


def get_number(text):
  while True:
    try:
      return int(input(text))
    except ValueError:
      print(" Enter a valid number.")

#add obstacles in robo's path
def add_obstacles(env, start, target):
  n = get_number("How many  obstacles would you like to add? ")


  for i in range(n):
    print(f"\nObstacle {i + 1}")
    x = get_number("X coordinate: ")
    y = get_number("Y coordinate: ")


    if (x, y) == start:
      print(" That's the robot's starting position.")

      continue

    if (x, y) == target:
      print("Oops! That's the target destination.")

      continue


    if env.blocked(x, y):
      print("An obstacle is already there.")
      continue


    env.add_obstacle(x, y)
    print(f"Successfully added obstacle at ({x}, {y})")


#ROBO's Status
def show_status(robot, target):
  print("\n--- ROBOT STATUS ---")
  print(f"Current Position: {robot.position()}")
  print(f"Target Position: {target}")
  print(f"Steps Taken: {robot.steps}")
  print(f"Battery Left: {robot.battery}%")
  print(f"Obstacles Avoided: {robot.avoided}")



def main():
  print("=== WELCOME TO ROBOROUTE ===")


  start_x = get_number("Starting X: ")
  start_y = get_number("Starting Y: ")


  target_x = get_number("Target X: ")
  target_y = get_number("Target Y: ")


  robot = Robot(start_x, start_y)
  env = Environment()


  start_pos = robot.position()
  target_pos = (target_x, target_y)


  add_obstacles(env, start_pos, target_pos)

  print(f"\nCurrent Obstacles List: {env.obstacles}")


  while True:
    print("\nWhat would you like to do?")
    print("1. Start Navigation")
    print("2. Check Robot Status")
    print("3. Show All Obstacles")
    print("4. Show Traveled Path")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
      success = navigate(robot, env, target_x, target_y)
      if success:
        print("Yay! The robot reached the target safely.")
      else:
        print("Sorry, the robot couldn't reach the target.")


    elif choice == "2":
      show_status(robot, target_pos)


    elif choice == "3":
      print(f"Obstacles: {env.obstacles}")


    elif choice == "4":
      print(f"Path history: {robot.path}")


    elif choice == "5":
      print("Exiting RoboRoute. Goodbye!!")
      break

    else:
      print("Invalid choice, select between 1 and 5.")


if __name__ == "__main__":
  main()

