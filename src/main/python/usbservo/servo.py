#!/usr/bin/env python

################################################
# Module:   servo.py
# Created:  2 April 2008
# Author:   Brian D. Wendt
#   http://principialabs.com/
# Version:  0.3
# License:  GPLv3
#   http://www.fsf.org/licensing/
'''
Provides a serial connection abstraction layer
for use with Arduino "MultipleSerialServoControl" sketch.
'''
################################################

import serial
import time
# Assign Arduino's serial port address
#   Windows example
#     usbport = 'COM3'
#   Linux example
#     usbport = '/dev/ttyUSB0'
#   MacOSX example
#     usbport = '/dev/tty.usbserial-FTALLOK2'
usbport = '/dev/tty.SLAB_USBtoUART'

# Set up serial baud rate
ser = serial.Serial(usbport, 9600, bytesize=8,stopbits=1,parity=serial.PARITY_NONE,timeout=1)


def command(servo, angle):
        ser.write(chr(255))
        ser.write(chr(0x1))
        ser.write(chr(0x0))
        ser.write(chr(0x14))
        ser.write(chr(0x0)) 
def command1(servo, angle):
        ser.write(chr(255))
        ser.write(chr(0x2))
        ser.write(chr(0x0))
        ser.write(chr(0xf4))
        ser.write(chr(0x01)) 
def command11(servo, angle):
        ser.write(chr(255))
        ser.write(chr(0x2))
        ser.write(chr(0x0))
        ser.write(chr(0xdc))
        ser.write(chr(0x05)) 
def command12(servo, angle):
        
        ser.write(chr(255))
        ser.write(chr(0x2))
        ser.write(chr(servo))
        ser.write(chr(angle%256))
        ser.write(chr(angle/256))         
        
def move(servo, angle):
    '''Moves the specified servo to the supplied angle.

    Arguments:
        servo
          the servo number to command, an integer from 1-4
        angle
          the desired servo angle, an integer from 0 to 180

    (e.g.) >>> servo.move(2, 90)
           ... # "move servo #2 to 90 degrees"'''

    if (0 <= angle <= 180):
        ser.write(chr(255))
        ser.write(chr(servo))
        ser.write(chr(angle))
    else:
        print "Servo angle must be an integer between 0 and 180.\n"

if __name__ == '__main__':
        command(1,10)
#        command11(1,10)
        command1(0,500)       
        time.sleep(10)
