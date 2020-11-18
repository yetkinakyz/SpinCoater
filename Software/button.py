import time
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

def button1(channel):
    print("1\n")
    time.sleep(0.1)


def button2(channel):
    print("2\n")
    time.sleep(0.1)


def button3(channel):
    print("3\n")
    time.sleep(0.1)


def button4(channel):
    print("4\n")
    time.sleep(0.1)


def button5(channel):
    print("5\n")
    time.sleep(0.1)


def button6(channel):
    print("6\n")
    time.sleep(0.1)

GPIO.setwarnings(False)

button1 = 38
button2 = 36
button3 = 34
button4 = 32
button5 = 30
button6 = 28

GPIO.setmode(GPIO.BOARD)
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
