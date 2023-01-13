# OOP's concept in python
# class
# Day 4
# class Person:
#     def __init__(self,name,address):
#         self.name=name
#         self.address=address

#     def show(self):
#         print(self.name)

# instant attribute = call within the constructor
# class attributes = call outside the constructor

# class Superheros:
#     def __init__(self, name, superpower):
#         self.name = name
#         self.superpower = superpower

#     def get_superpower(self):
#         print(f"I am {self.name} and my power is {self.superpower}")


# ironman = Superheros(
#     name="Iron Man",
#     superpower="Suit"
# )
# ironman.get_superpower()

# thor = Superheros(
#     name="Thor",
#     superpower="Ssso"
# )
# thor.get_superpower()

# class Sensor(): = name, location, record_dates,
# Ac(),Gy(),Gps()    (app.py(server me run kr rha h))


import numpy as np


class Sensor:
    def __init__(self, name, location, record_date):
        self.name = name
        self.location = location
        self.record_date = record_date
        self.data = {}  # blank dict when data comes from sensor we can add the data inside the constructor

    def add_data(self, data, time):
        self.data["data"] = data
        self.data["time"] = time
        print("Data points added successfully")

        def clear_data(self):
            self.data = {}
            print("Data points deleted successfully")


sensor1 = Sensor(
    name="sensor1",
    location="Haldia",
    record_date="2023-01-09"
)

# here data is global variable or attribute  (concept of init.py)
data = np.random.randint(-10, 10, 10)
time = np.arange(10)
print(time)

sensor1.add_data(
    data=data,  # data is function parameter
    time=time
)
# this data is dictionary attribute  in line 48
print("Generic Sensic Data:", sensor1.data)


class Accelerometer(Sensor):

    def show_sensor_type(self):
        print(f"This is {self.name}")


acc_data = np.random.randint(-10, 10, 10)
acc_time = np.arange(10)

acc = Accelerometer("Accl", "Haldia", "2023-01-09")


class Gyro(Accelerometer):
    def show_sensor_type(self):
        print(f"This is {self.name} and the location is {self.location}")


gyro_data = np.random.randint(-15, 15, 10)
gyro_time = np.arange(10)

gyro = Gyro(
    name="Gyroscope",
    location="Kolkata",
    record_date="2023-01-10"
)

gyro.add_data(time=gyro_time, data=gyro_data)

acc.show_sensor_type()
gyro.show_sensor_type()


acc.add_data(
    data=acc_data,
    time=acc_time

)
print("Accelerometer Data", acc)

# GPS attributes:
# name
# location
# record_date
# brand


class GPS(Sensor):
    def __init__(self, name, location, record_date, brand):
        super().__init__(
            name, location, record_date
        )
        self.brand = brand


gps = GPS(
    name="GPS",
    location="Muzaffarpur",
    record_date="2023-01-10",
    brand="espressif"
)

print(gps.name)
print(gps.location)
print(gps.record_date)
print(gps.brand)
