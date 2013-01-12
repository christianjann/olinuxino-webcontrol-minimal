#!/usr/bin/env python
# coding=utf8

def ledon():
    value = open("/sys/class/leds/green/brightness","w")
    value.write(str(1))
    value.close()

def ledoff():
    value = open("/sys/class/leds/green/brightness","w")
    value.write(str(0))
    value.close()

def ledheartbeat():
    value = open("/sys/class/leds/green/trigger","w")
    value.write("heartbeat")
    value.close()

def export_pins(pins):
    try:
        f = open("/sys/class/gpio/export","w")
        f.write(str(pins))
        f.close()
    except IOError:
        print "GPIO %s already Exists, so skipping export gpio" % (str(pins), )

def unexport_pins(pins):
    try:
        f = open("/sys/class/gpio/unexport","w")
        f.write(str(pins))
        f.close()
    except IOError:
        print "GPIO %s is not found, so skipping unexport gpio" % (str(pins), )

def setpindirection(pin_no, pin_direction):
    gpiopin = "gpio%s" % (str(pin_no), )
    pin = open("/sys/class/gpio/"+gpiopin+"/direction","w")
    pin.write(pin_direction)
    pin.close()

def writepins(pin_no, pin_value):
    gpiopin = "gpio%s" % (str(pin_no), )
    pin = open("/sys/class/gpio/"+gpiopin+"/value","w")
    if pin_value == 1:
      pin.write("1")
    else:
      pin.write("0")
    pin.close()

def readpins(pin_no):
    gpiopin = "gpio%s" % (str(pin_no), )
    pin = open("/sys/class/gpio/"+gpiopin+"/value","r")
    value = pin.read()
    print "The value on the PIN %s is : %s" % (str(pin_no), str(value))
    pin.close()
    return int(value)

if __name__ == '__main__':
    from time import sleep
    export_pins(32)
    setpindirection(32, "out")

    while(1):
      ledon()
      writepins(32, 1)
      sleep(1)
      ledoff()
      writepins(32, 0)
      sleep(1)
