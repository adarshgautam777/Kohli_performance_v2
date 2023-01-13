import numpy as np
import sensor as s




# here data is global variable or attribute  (concept of init.py)



# this data is dictionary attribute  in line 48



acc_data = np.random.randint(-10, 10, 10)
acc_time = np.arange(10)

acc = s.Accelerometer("Accl", "Haldia", "2023-01-09")


gyro_data = np.random.randint(-15, 15, 10)
gyro_time = np.arange(10)

gyro = s.Gyro(
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


gps = s.GPS(
    name="GPS",
    location="Muzaffarpur",
    record_date="2023-01-10",
    brand="espressif"
)

print(gps.name)
print(gps.location)
print(gps.record_date)
print(gps.brand)
