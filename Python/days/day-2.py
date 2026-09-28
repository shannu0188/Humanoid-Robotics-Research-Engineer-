# its a day2 now i'm practice 
# class HumanoidRobot:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height

#     def walk(self):
#         print(self.name, "is walking")


# robot = HumanoidRobot("H1", 1.8)

# robot.walk()

# class robot:
#     pass
# robot1 = robot()
# robot2 = robot()

# print(robot1)
# print(robot2)

# class Robot:
#     def __init__(self):
#         print("Robot created")

# robot1 = Robot()

# class robot:
#     def __init__(self):
#         print(" alita robot created")
    
# robot1 = robot()

class Robot:
    def walk(self):
        print("Walking")

    def stop(self):
        print("Stopped")

    def turn(self):
        print("Turning")

robot = Robot()
robot.walk()
robot.stop()
robot.turn()

sensor_values = [20, 35, 40, 28, 50]

# Creating a list
motor_angles = [10, 25, 40, 15, 30]

# Accessing elements
print(motor_angles[0])
print(motor_angles[2])

# Adding an element
motor_angles.append(45)

# Removing an element
motor_angles.remove(25)

# Modifying an element
motor_angles[0] = 15

# Printing the final list
print(motor_angles)
