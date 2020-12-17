'''
SPIN COATER PROJECT RPM CONTROL SOFTWARE
                        by Yetkin AKYUZ

    Website: https://yetkinakyuz.com
    Email:   contact@yetkinakyuz.com
'''

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

# MOTOR
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

# IR SENSOR 
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

sampleRpmList = [ 500, 800,
            1000, 1200, 1500, 1800,
            2000, 2200, 2500, 2800,
            3000, 3200, 3500, 3800,
            4000, 4200, 4500, 4800,
            5000, 5200, 5500, 5800,
            6000, 6200, 6500, 6800,
            7000, 7200]         
sampleSpeedList = [ 4.7, 6,
                    6.7, 7.5, 8.5, 10,
                    10.5, 11.5, 13, 14.5,
                    15.5, 16.8, 18.5, 20,
                    21.5, 23, 25, 27.5,
                    30, 32, 35.5, 38,
                    40.5, 44.0, 48.0, 53.0,
                    55.5, 60.5]
cycleRpmList= []
cycleList = []

firstStage = True
done = False

expectedRPM = 0
expectedTime = 0

# Getters & Setters
def setExpectedRPM(n):
    global expectedRPM
    expectedRPM = n

def getExpectedRPM():
    return expectedRPM

def setExpectedTime(n):
    global expectedTime
    expectedTime = n
    
def getExpectedTime():
    return expectedTime

## Modules

def clear():
    global sample
    global count
    global rpm
    global start
    global end
    global done
    global firstStage
    global speed

    sample = 3
    count = 0
    rpm = 0
    start = 0
    end = 0
    speed = 0

    done = False
    firstStage = True

    setExpectedRPM(0)
    setExpectedTime(0)

    motor.start(0)
    GPIO.output(motor_in1,GPIO.HIGH)

    display.lcd_clear()

def done():
    global done
    done = True
    GPIO.output(motor_in1,GPIO.LOW)

# FIRST STAGE
def FirstStage():
    global speed
    global firstStage
    global done

    print(getExpectedRPM())
    print(getExpectedTime())

    for i in sampleRpmList:

        if getExpectedRPM() >= i - 100 and getExpectedRPM() <= i + 100:
            
            print("\ngetRPM=" + str(i))
            print("\ngetSpeed=" + str(sampleSpeedList[sampleRpmList.index(i)])+"\n")

            speed = sampleSpeedList[sampleRpmList.index(i)]
            
            print("\nSpeed=" + str(speed) + "\n")

        else:
            continue

    motor.ChangeDutyCycle(speed)

    time.sleep(1)
  
    while True:
       
        t_end = getExpectedTime()

        display.lcd_clear()
        display.lcd_display_string("TIME :       SEC", 1) #PRINT LINE 1
        display.lcd_display_string("SPEED:       RPM", 2) #PRINT LINE 2

        time.sleep(2)

        while t_end >= 0:
            for j in range(1):
                if t_end >= 0:
                    display.lcd_display_string("TIME :       SEC", 1) #PRINT LINE 1
                    display.lcd_display_string("SPEED:       RPM", 2) #PRINT LINE 2
                    display.lcd_display_string("TIME : " + str(t_end), 1) #PRINT LINE 1
                    display.lcd_display_string("SPEED: " + str(rpm), 2) #PRINT LINE 2

                    time.sleep(1)
                    t_end = t_end - 1

                    for i in range(1):
                        if t_end >= 0:
                            display.lcd_display_string("TIME :       SEC", 1) #PRINT LINE 1
                            display.lcd_display_string("TIME : " + str(t_end), 1) #PRINT LINE 1

                            time.sleep(1)
                            t_end = t_end - 1
                        else:
                            break
                else:
                    break

        firstStage = False

        break #Break the RpmControl

# NEXT STAGE
def NextStage():
    global speed
    global done

    print(getExpectedRPM())
    print(getExpectedTime())

    for i in sampleRpmList:

        if getExpectedRPM() >= i - 100 and getExpectedRPM() <= i + 100:
            
            print("\ngetRPM=" + str(i))
            print("\ngetSpeed=" + str(sampleSpeedList[sampleRpmList.index(i)])+"\n")

            speed = sampleSpeedList[sampleRpmList.index(i)]
            
            print("\nSpeed=" + str(speed) + "\n")

        else:
            continue

    motor.ChangeDutyCycle(speed)

    while True:
            
        t_end = getExpectedTime()

        while t_end >= 0:
            for j in range(1):
                if t_end >= 0:
                    display.lcd_display_string("TIME :       SEC", 1) #PRINT LINE 1
                    display.lcd_display_string("SPEED:       RPM", 2) #PRINT LINE 2
                    display.lcd_display_string("TIME : " + str(t_end), 1) #PRINT LINE 1
                    display.lcd_display_string("SPEED: " + str(rpm), 2) #PRINT LINE 2

                    time.sleep(1)
                    t_end = t_end - 1

                    for i in range(1):
                        if t_end >= 0:
                            display.lcd_display_string("TIME :       SEC", 1) #PRINT LINE 1
                            display.lcd_display_string("TIME : " + str(t_end), 1) #PRINT LINE 1

                            time.sleep(1)
                            t_end = t_end - 1
                        else:
                            break
                else:
                    break

        break #Break the RpmControl

# SET SAMPLE
def SetSample(rpm):
    global sample

    if rpm >= 500 and rpm <= 1500:
        sample = 30

    elif rpm > 1500 and rpm <= 2500:
        sample = 45

    elif rpm > 2500 and rpm <= 3500:
        sample = 60

    elif rpm > 3500 and rpm <= 4500:
        sample = 75

    elif rpm > 4500:
        sample = 90
    
    return sample

#MOTOR SPEED CONTROL
def SpeedControl(expected, current, previous):   
    global speed
    global done

    if done == True:       
        done()

    else:
        n = expected - current
        error = 5*expected/100 # Error is 5%

        print("\nspeed: " + str(speed))
        print("expected: " + str(s))
        print("rpm: " + str(r) + "\n")

        if current == 0 or current == previous:
            print("---")

        elif (n > error):
            speed = speed + 0.1
            motor.ChangeDutyCycle(speed)

            print("LOW")

        elif (n < -error):
            speed = speed - 0.1
            motor.ChangeDutyCycle(speed)

            print("HIGH")

        else:
            print("NEUTRAL")

#SET START TIME
def set_start():
    global start
    start = time.time()

#SET END TIME
def set_end(): 
        global end
        end = time.time()

# GET RPM
def get_rpm(channel):
    global count
    global sample
    global rpm
        
    if count == 0: 
            set_start()        
            count = count + 1
    
    elif count == SetSample(rpm):
            set_end()

            rpm_pre = rpm

            delta = end - start
            delta = delta / 60

            rpm = int((sample/delta)/2)

            count = 0

            SpeedControl(getExpectedRPM(), rpm, rpm_pre)
    
    else:
        count = count + 1

GPIO.add_event_detect(ir_sensor, GPIO.FALLING, callback = get_rpm)

