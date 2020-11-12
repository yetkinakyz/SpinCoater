import time
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

def button1(channel):
    print("1\n")


def button2(channel):
    print("2\n")


def button3(channel):
    print("3\n")


def button4(channel):
    print("4\n")


def button5(channel):
    print("5\n")


def button6(channel):
    print("6\n")


GPIO.setwarnings(False) # Ignore warning for now

GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(0, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(0,GPIO.RISING,callback=button1)
GPIO.add_event_detect(5,GPIO.RISING,callback=button2)
GPIO.add_event_detect(6,GPIO.RISING,callback=button3)
GPIO.add_event_detect(13,GPIO.RISING,callback=button4)
GPIO.add_event_detect(19,GPIO.RISING,callback=button5)
GPIO.add_event_detect(26,GPIO.RISING,callback=button6)

input()