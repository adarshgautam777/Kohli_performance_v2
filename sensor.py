import numpy as np
import sensorModule as Sensor


class Accelerometer(Sensor.Sensor):

    def show_sensor_type(self):
        print(f"This is {self.name}")


class Gyro(Accelerometer):
    def show_sensor_type(self):
        print(f"This is {self.name} and the location is {self.location}")




# GPS attributes:
# name
# location
# record_date
# brand


class GPS(Sensor.Sensor):
    def __init__(self, name, location, record_date, brand):
        super().__init__(
            name, location, record_date
        )
        self.brand = brand


