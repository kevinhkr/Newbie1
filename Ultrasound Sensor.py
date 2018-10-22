from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=18, trigger=4, queue_len=10)

while True:
    print('Distance to nearest object is', sensor.get_distance, 'm')
    sleep(0.5)
