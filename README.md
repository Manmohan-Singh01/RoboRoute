## RoboRoute – Smart Robot Navigation

## About the Project

RoboRoute is a Python-based robot navigation and pathfinding project.

In this project, the user gives the robot a starting position and a target position. The user can also add obstacles in the environment. The robot then tries to reach the target while avoiding the obstacles.

The program also keeps track of the robot's position, number of steps, battery level, avoided obstacles, and travelled path.

---

## Features

* Set the starting position of the robot
* Set the target position
* Add obstacles manually
* Prevent obstacles from being placed on the start or target
* Check for duplicate obstacles
* Navigate the robot to the target
* Show the robot's current status
* Display all obstacles
* Display the travelled path
* Track steps taken
* Track battery level
* Track obstacles avoided
* Menu-based interface

---

## Project Structure

RoboRoute/
│
├── RoboRoute_main.py
├── robot.py
├── environment.py
├── navigation.py
└── README.md

### `RoboRoute_main.py`

This is  the main file of the project.

It takes input from the user, creates the robot and environment, adds obstacles, and provides the menu.

### `robot.py`

This file contains the `Robot` class.

It stores information such as:

* Robot position
* Steps taken
* Battery level
* Obstacles avoided
* Travelled path

### `environment.py`

This file contains the `Environment` class.

It manages the obstacles in the robot's environment.

### `navigation.py`

This file contains the navigation logic.

It is responsible for moving the robot towards the target while dealing with obstacles.

---

## Technologies Used

* Python 3.14
* Object-Oriented Programming
* Functions
* Classes and Objects
* Lists and Tuples
* Loops
* Conditional Statements
* Exception Handling
* Python Modules

---

## Requirements

* Python 3.14.7
* VS Code 

---
## Dependencies
This project usesPython standard libraries only.
No external packages are required.

## How to Run

1. Open the RoboRoute project folder in VS Code.
2. Make sure all four Python files are in the same folder.
3. Open `RoboRoute_main.py`.
4. Run the program.

For example:

```
python RoboRoute_main.py
```

---

## How the Program Works

First, the program asks for the robot's starting X and Y coordinates.

Then it asks for the target X and Y coordinates.

Example:

```
Starting X: 0
Starting Y: 0

Target X: 5
Target Y: 5
```

After this, the user can enter the number of obstacles and their coordinates.

Example:

```
How many obstacles? 3

Obstacle 1
Enter X: 2
Enter Y: 0

Obstacle 2
Enter X: 2
Enter Y: 1

Obstacle 3
Enter X: 4
Enter Y: 3
```

The program then displays a menu.

```
--- MENU ---
1. Start Navigation
2. Check Robot Status
3. Show Obstacles
4. Show Traveled Path
5. Exit
```

The user can select an option according to what they want to see.

---

## Example Output

```
=== ROBOROUTE ===

Starting X: 0
Starting Y: 0
Target X: 5
Target Y: 5

How many obstacles? 2

Obstacle 1
Enter X: 2
Enter Y: 1
Obstacle added at (2, 1)

Obstacle 2
Enter X: 3
Enter Y: 3
Obstacle added at (3, 3)

--- MENU ---
1. Start Navigation
2. Check Robot Status
3. Show Obstacles
4. Show Traveled Path
5. Exit

Enter choice: 1

Robot reached the target!
```

---

## Robot Status

The status option displays information about the robot.

Example:

```
--- ROBOT STATUS ---
Position: (5, 5)
Target: (5, 5)
Steps: 10
Battery: 90 %
Avoided: 2
```

---

## Input Validation

The program checks whether the user enters a valid number.

It also checks that:

* An obstacle is not placed at the starting position.
* An obstacle is not placed at the target position.
* The same obstacle is not added twice.

---

## Objective

The main objective of this project is to demonstrate how Python can be used to create a simple robot navigation system using programming concepts such as classes, functions, conditions, loops, modules, and user input.

---

## Future Improvements

Some features that can be added later are:

* Graphical user interface
* Visual grid for the robot
* More advanced pathfinding algorithms
* Different types of obstacles
* Recharge stations for the robot
* Multiple robots
* Automatic obstacle generation
* Save and load previous routes

---

## Conclusion

RoboRoute is a robot navigation and pathfinding simulation made using Python. It combines object-oriented programming, modular programming, input handling, and navigation logic into one project.

The project can also be extended with more advanced navigation and visualization features in the future.