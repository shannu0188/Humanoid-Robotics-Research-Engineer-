# i have already done some data types now just create a file 
# def greet():
#     print("hello robot")
# greet()

# def robot_status(name, battery):
#     print(f"robot {name} is ready ! \n Alita health is {battery} %")
# robot_status("Alita", 85)

# def robot_status(name, battery, temprature):
#     print(f"robot {name} is ready !")
#     if battery <= 20:
#         print("WARNING ! LOW BATTERY !")
#     else:
#         print(f"Alita health is ok ")

#     if temprature > 40:
#         print("WARNING ! HIGH TEMPERATURE !")
#     else:
#         print(f"Alita temprature is ok ")
# robot_status("Alita", 15, 41)

# import time
# for i in range(5):
#     print("checking ...!")
#     time.sleep(1)  
# time.sleep(1)
# print("Alita is ready 😉")

# import time
# print("checking ...!")
# time.sleep(1)
# print("Alita is ready")

# import time
# count = 1
# while count <= 5:
#     print(f" robot checking ...! {count}")
#     time.sleep(1)
#     count = count + 1

# import time
# sensor_active = True
# while sensor_active:
#     print("robot is scanning ...!")
#     time.sleep(1)

#     sensor_active = False
# print("scanning stop")
# import time
# count = 1
# while count <= 10:
#     print(f"robot checking ...! {count}")
#     time.sleep(1)

#     if count == 5:
#         print("Emergency Stop ⚠️")
#         break
#     count = count + 1

# for i in range(1, 10):
#     print(f"robot checking ...! {i}")
#     time.sleep(1)

#     if i == 5:
#         print("Emergency Stop ⚠️")
#         break
# import time

# for i in range(1, 6):
#     if i == 3:
#         continue
#     time.sleep(1)
#     print(f"robot checking ...! {i}")

sensors = ["camera", "lider", "ultrasonic", "temprature"]
for sensor in sensors:
    print(f"checking {sensor} sensor ...!")
