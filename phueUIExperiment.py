from phue import Bridge
from time import sleep
import random

b = Bridge('192.168.2.23')
pLight = b.get_light_objects()[0]

#Menu loop
while True:
    print(
        "JTL Phue Mediated Hue Controller"
    )
    inp = input()

    break