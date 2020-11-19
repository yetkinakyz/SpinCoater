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

# OTHERS
expectedRPM = 0
expectedTime = 0

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

check = False
firstTime = True
stop = False

GPIO.add_event_detect(ir_sensor, GPIO.FALLING, callback = get_rpm)

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
    global expectedRPM

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

                speed_control(expectedRPM, rpm, rpm_pre)
        
        else:
            count = count + 1

#STOP
def stop(self):
    stop = True       
    return stop

#START
def start(k, l):
    global speed
    global stop

    display.lcd_clear()

    expectedRPM = int(k)
    expectedTime = int(l)

    print(expectedRPM)
    print(expectedTime)

    display.lcd_clear()
    display.lcd_display_string("    MOTOR IS    ",1) #PRINT LINE 1
    display.lcd_display_string("  ACCELERATING  ",2) #PRINT LINE 1

    for i in sampleRpmList:

        if expectedRPM >= i - 100 and expectedRPM <= i + 100:
            
            print("\ngetRPM=" + str(i))
            print("\ngetSpeed=" + str(sampleSpeedList[sampleRpmList.index(i)])+"\n")

            speed = sampleSpeedList[sampleRpmList.index(i)]
            
            print("\nSpeed=" + str(speed) + "\n")

        else:
            continue

    motor.ChangeDutyCycle(speed)


    while True:
        if stop:
            speed = 0
            motor.ChangeDutyCycle(speed)
            print(speed)
        
            break

        else:
            if check == False:
                if firstTime:
                    print("SLEEPING...")
                    time.sleep(1)

                else:
                    print("ACCELERATING...")
                    time.sleep(1)
                
            else:
                print("ACCELERATED!")
                
                t_end = expectedTime

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

    return True
