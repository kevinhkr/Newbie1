import gpiozero
from gpiozero import DistanceSensor
import time

sensor = DistanceSensor(echo=18, trigger=4, queue_len=10)

red = gpiozero.LED(17)


while sensor.get_distance < 20:
    red.on()
    time.sleep(0.5)
    red.off()
    time.sleep(0.5)
