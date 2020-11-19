##### LIBRARIES #####
import RPi.GPIO as GPIO #RASPBERRY PI GPIO LIBRARY WIKI: https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/
import lcddriver #LCD I2C LIBRARY
import time

##### SETUP ##### 

## DISPLAY
display = lcddriver.lcd()

## GPIO
GPIO.setwarnings(False) #DISABLE WARNINGS
GPIO.setmode(GPIO.BCM) #GPIO PIN NUMBERS (GPIO.BOARD for physical pin numbers.)

## BUTTONS
button1 = 0
button2 = 5
button3 = 6
button4 = 13
button5 = 19
button6 = 26

GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

buttonState1 = GPIO.input(button1)
buttonState2 = GPIO.input(button2)
buttonState3 = GPIO.input(button3)
buttonState4 = GPIO.input(button4)
buttonState5 = GPIO.input(button5)
buttonState6 = GPIO.input(button6)

## MOTOR
motor_in1 = 23 #MOTOR IN 1
motor_in2 = 24 #MOTOR IN 2

motor_en = 25 #MOTOR SPEED CONTROL PIN

# GPIO outputs
GPIO.setup(motor_in1,GPIO.OUT)
GPIO.setup(motor_in2,GPIO.OUT)
GPIO.setup(motor_en,GPIO.OUT)

# Motor turns clockwise
GPIO.output(motor_in1,GPIO.HIGH)
GPIO.output(motor_in2,GPIO.LOW)

motor=GPIO.PWM(motor_en,1000)

motor.start(0) #MOTOR START SPEED
speed = 0

## IR SENSOR 
ir_sensor = 22 #GPIO PIN

GPIO.setmode(GPIO.BCM)
GPIO.setup(ir_sensor,GPIO.IN)

# get_rpm(channel) variables
sample = 3
count = 0
rpm = 0

# set_start() and set_end() variables
start = 0
end = 0

# OTHERS
sampleRpmList = [ 100, 200, 300, 400, 500, 800,
            1000, 1200, 1500, 1800,
            2000, 2200, 2500, 2800,
            3000, 3200, 3500, 3800,
            4000, 4200, 4500, 4800,
            5000, 5200, 5500, 5800,
            6000, 6200, 6500, 6800,
            7000, 7200]         
sampleSpeedList = [ 2.8, 3.3, 3.8, 4.2, 4.7, 6,
                    6.7, 7.5, 8.5, 10,
                    10.5, 11.5, 13, 14.5,
                    15.5, 16.8, 18.5, 20,
                    21.5, 23, 25, 27.5,
                    30, 32, 35.5, 38,
                    40.5, 44.0, 48.0, 53.0,
                    55.5, 60.5]
cycleRpmList= []
cycleList = []

expected = -1
t = 0
inpt = -1

check = False
firstTime = True

##### FUCTIONS #####

#SET START TIME
def set_start():
 	global start
 	start = time.time()

#SET END TIME
def set_end(): 
        global end
        end = time.time()

#MOTOR SPEED CONTROL
def speed_control(c, r, p):   
    global speed
    global check

    n = c - r

    print("\nspeed: " + str(speed))
    print("expected: " + str(c))
    print("rpm: " + str(r) + "\n")

    if r == 0 or r == p:
        print("---")

    elif (n > 50):
        speed = speed + 0.1
        motor.ChangeDutyCycle(speed)

        print("LOW")

    elif (n < -50):
        speed = speed - 0.1
        motor.ChangeDutyCycle(speed)

        print("HIGH")

    else:
        check = True
        print("NEUTRAL")

# SET SAMPLE
def setSample(rpm):
    global sample

    if rpm < 250:
        sample = 3

    elif rpm > 250 and rpm < 400:
        sample = 12

    elif rpm > 400 and rpm < 560:
        sample = 24

    elif rpm > 560 and rpm < 1000:
        sample = 30

    elif rpm > 1000 and rpm < 3500:
        sample = 60

    elif rpm > 3500:
        sample = 120
    
    return sample

# BUTTON CHECK
def checkButton():
    global buttonState1
    global buttonState2
    global buttonState3
    global buttonState4
    global buttonState5
    global buttonState6

    if (not buttonState1):
        return 1
        time.sleep(0.5)

    elif (buttonState2):
        return 2
        time.sleep(0.5)

    elif (buttonState3):
        return 3
        time.sleep(0.5)

    elif (buttonState4):
        return 4
        time.sleep(0.5)

    elif (buttonState5):
        return 5
        time.sleep(0.5)

    elif (buttonState6):
        return 6
        time.sleep(0.5)

    else:
        return 0

# GET RPM
def get_rpm(channel):
    global count
    global sample

    global expected
    global rpm

    global firstTime

    if firstTime:
        time.sleep(5)
        firstTime = False

    else:
        
        if count == 0: 
                set_start()        
                count = count + 1
        
        elif count == setSample(rpm):
                set_end()

                rpm_pre = rpm

                delta = end - start
                delta = delta / 60

                rpm = int((sample/delta)/2)

                count = 0

                speed_control(expected, rpm, rpm_pre)
        
        else:
            count = count + 1

#DISPLAY RECENT
def displayRecent():
    global t
    global rpm

    checkButton()

    if checkButton() == 1:
        display.lcd_clear()
        display.lcd_display_string("SET:    " + str(t) + " SEC",1) #PRINT LINE 1
        display.lcd_display_string("        " + str(expected) +" RPM",2) #PRINT LINE 2

    else:
        display.lcd_clear()

        if check == False:
            if firstTime:
                print("SLEEPING...")
                time.sleep(1)

            else:
                print("ACCELERATING...")
                time.sleep(1)
            
        else:
            print("ACCELERATED!")
            
            t_end = t

            time.sleep(1)

            display.lcd_clear()

            display.lcd_display_string("TIME :       SEC", 1) #PRINT LINE 1
            display.lcd_display_string("SPEED:       RPM", 2) #PRINT LINE 2

            while t_end > 0:
                for j in range(2):
                    display.lcd_display_string("TIME :       SEC", 1) #PRINT LINE 1
                    display.lcd_display_string("SPEED:       RPM", 2) #PRINT LINE 2
                    display.lcd_display_string("TIME : " + str(t_end), 1) #PRINT LINE 1
                    display.lcd_display_string("SPEED: " + str(rpm), 2) #PRINT LINE 2

                    time.sleep(1)
                    t_end = t_end - 1

                    for i in range(2):
                        display.lcd_display_string("TIME :       SEC", 1) #PRINT LINE 1
                        display.lcd_display_string("TIME : " + str(t_end), 1) #PRINT LINE 1

                        time.sleep(1)
                        t_end = t_end - 1

### ### ### ### ###

## IR SENSOR DETECT ##
GPIO.add_event_detect(ir_sensor, GPIO.FALLING, callback=get_rpm)

try:
    while True:
        checkButton()
        displayRecent()

except KeyboardInterrupt: 
    GPIO.cleanup()