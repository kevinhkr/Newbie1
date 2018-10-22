import gpiozero
import time

red = gpiozero.LED(17)

freq = int(input("Set Frequency(Hz): "))
a = 1/freq

while True:
    red.on()
    time.sleep(a)
    red.off()
    time.sleep(a)
