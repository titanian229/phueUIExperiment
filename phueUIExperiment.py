from phue import Bridge
from time import sleep
import random

b = Bridge('192.168.2.23')
pLight = b.get_light_objects()[0]

#Menu loop
while True:
    print(
        """JTL Phue Mediated Hue Controller
        Options
        1. Toggle Light State
        2. Modify Brightness
        3. Change Colour"""
    )
    inp = input("Enter option : ")

    inp_options = ['1', '2', '3', 'x']

    if not inp in inp_options:
        print('Please enter a valid choice')

    if inp == '1':

        pLight.on = not pLight.on
    elif inp == '2':

        print('Set brightness from 0-1 or 1-255')
        b_inp = input(' : ')

        pLight.brightness = int(b_inp)

    elif inp == '3':

        xVal = input('Enter x value : ')
        yVal = input('Enter y value : ')
        pLight.xy = [int(xVal), int(yVal)]


    elif inp == 'x':
        break