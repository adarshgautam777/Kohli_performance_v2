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


