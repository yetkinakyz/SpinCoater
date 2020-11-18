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

button1 = 26
button2 = 19
button3 = 13
button4 = 6
button5 = 5
button6 = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(button1, GPIO.IN)
GPIO.setup(button2, GPIO.IN)
GPIO.setup(button3, GPIO.IN)
GPIO.setup(button4, GPIO.IN)
GPIO.setup(button5, GPIO.IN)
GPIO.setup(button6, GPIO.IN)

'''
GPIO.add_event_detect(0,GPIO.RISING,callback=button1, bouncetime=500)
GPIO.add_event_detect(5,GPIO.RISING,callback=button2, bouncetime=500)
GPIO.add_event_detect(6,GPIO.RISING,callback=button3, bouncetime=500)
GPIO.add_event_detect(13,GPIO.RISING,callback=button4, bouncetime=500)
GPIO.add_event_detect(19,GPIO.RISING,callback=button5, bouncetime=500)
GPIO.add_event_detect(26,GPIO.RISING,callback=button6, bouncetime=500)
'''
while True:
    buttonState1 = GPIO.input(button1)
    buttonState2 = GPIO.input(button2)
    buttonState3 = GPIO.input(button3)
    buttonState4 = GPIO.input(button4)
    buttonState5 = GPIO.input(button5)
    buttonState6 = GPIO.input(button6)

    if (buttonState1):
        button1()
        time.sleep(0.1)

    elif (buttonState2):
        button2()
        time.sleep(0.1)

    elif (buttonState3):
        button3()
        time.sleep(0.1)

    elif (buttonState4):
        button4()
        time.sleep(0.1)

    elif (buttonState5):
        button5()
        time.sleep(0.1)

    elif (buttonState6):
        button6()
        time.sleep(0.1)

    else:
        continue

    input()
