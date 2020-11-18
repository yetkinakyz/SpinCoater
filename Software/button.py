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
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

'''
GPIO.add_event_detect(0,GPIO.RISING,callback=button1, bouncetime=500)
GPIO.add_event_detect(5,GPIO.RISING,callback=button2, bouncetime=500)
GPIO.add_event_detect(6,GPIO.RISING,callback=button3, bouncetime=500)
GPIO.add_event_detect(13,GPIO.RISING,callback=button4, bouncetime=500)
GPIO.add_event_detect(19,GPIO.RISING,callback=button5, bouncetime=500)
GPIO.add_event_detect(26,GPIO.RISING,callback=button6, bouncetime=500)
'''
while True:
    i = False

    buttonState1 = GPIO.input(button1)
    buttonState2 = GPIO.input(button2)
    buttonState3 = GPIO.input(button3)
    buttonState4 = GPIO.input(button4)
    buttonState5 = GPIO.input(button5)
    buttonState6 = GPIO.input(button6)

    if (buttonState1):

        while (not i):
            print("1\n")
            time.sleep(0.2)

            i = True

    elif (buttonState2):

        while (not i):
            print("2\n")
            time.sleep(0.2)

            i = True

    elif (buttonState3):

        while (not i):
            print("3\n")
            time.sleep(0.2)

            i = True

    elif (buttonState4):

        while (not i):
            print("4\n")
            time.sleep(0.2)

            i = True

    elif (buttonState5):

        while (not i):
            print("5\n")
            time.sleep(0.2)

            i = True

    elif (not buttonState6):

        while (not i):
            print("6\n")
            time.sleep(0.2)

            i = True

    else:
        continue

    time.sleep(0.1)

input()
