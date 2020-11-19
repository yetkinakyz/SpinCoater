import time
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

def button1():
    print("1\n")
    time.sleep(0.1)


def button2():
    print("2\n")
    time.sleep(0.1)


def button3():
    print("3\n")
    time.sleep(0.1)


def button4():
    print("4\n")
    time.sleep(0.1)


def button5():
    print("5\n")
    time.sleep(0.1)


def button6():
    print("6\n")
    time.sleep(0.1)

GPIO.setwarnings(False)

button1 = 0
button2 = 5
button3 = 6
button4 = 13
button5 = 19
button6 = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


GPIO.add_event_detect(0,GPIO.BOTH,callback=button1, bouncetime=500)
GPIO.add_event_detect(5,GPIO.BOTH,callback=button2, bouncetime=500)
GPIO.add_event_detect(6,GPIO.BOTH,callback=button3, bouncetime=500)
GPIO.add_event_detect(13,GPIO.BOTH,callback=button4, bouncetime=500)
GPIO.add_event_detect(19,GPIO.BOTH,callback=button5, bouncetime=500)
GPIO.add_event_detect(26,GPIO.BOTH,callback=button6, bouncetime=500)

input()
