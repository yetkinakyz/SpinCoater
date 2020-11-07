##### LIBRARIES #####
import RPi.GPIO as GPIO #RASPBERRY PI GPIO LIBRARY WIKI: https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/
import lcddriver #LCD I2C LIBRARY
import time

##### SETUP ##### 
display = lcddriver.lcd()

# MOTOR
motor_in1 = 23
motor_in2 = 24

motor_en = 25

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(motor_in1,GPIO.OUT)
GPIO.setup(motor_in2,GPIO.OUT)

GPIO.setup(motor_en,GPIO.OUT)

GPIO.output(motor_in1,GPIO.HIGH)
GPIO.output(motor_in2,GPIO.LOW)

motor=GPIO.PWM(motor_en,50)
motor.start(0)

speed = 0

# IR SENSOR 
ir_sensor = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(ir_sensor,GPIO.IN)

sample = 3
count = 0

start = 0
end = 0

rpm = 0

expected = -1
inpt = -1

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

    n = c - r

    print(str(speed)+"\n")
    print(str(c))
    print(str(r) + "\n")

    if r == 0 or r == p:
        print("N")

    elif (n > 25):
        speed = speed + 0.1
        motor.ChangeDutyCycle(speed)
        print("LOW")

    elif (n < -25):
        speed = speed - 0.1
        motor.ChangeDutyCycle(speed)
        print("HIGH")

    else:
        print("N")

# GET RPM
def get_rpm(c):
    global count
    global sample

    global expected
    global rpm

    if rpm < 250:
        sample = 3

    elif rpm > 250 and rpm < 400:
        sample = 6

    elif rpm > 400 and rpm < 560:
        sample = 9

    elif rpm > 560 and rpm < 1000:
        sample = 15

    elif rpm > 1000 and rpm < 3500:
        sample = 30

    elif rpm > 3500:
        sample = 60
    
    if count == 0: 
            set_start()        
            count = count + 1
    else:
        count = count + 1
            
    if count == sample:
            set_end()

            rpm_pre = rpm

            delta = end - start
            delta = delta / 60

            rpm = int((sample/delta)/2)

            count = 0

            speed_control(expected, rpm, rpm_pre)

print("Welcome!\n")

display.lcd_display_string("  SPIN  COATER  ", 1) #PRINT LINE 1
display.lcd_display_string(" RPM CONTROLLER ", 2) #PRINT LINE 2
time.sleep(2)

display.lcd_display_string("       BY       ", 1) #PRINT LINE 1
display.lcd_display_string("  YETKIN AKYUZ  ", 2) #PRINT LINE 2
time.sleep(2)

display.lcd_display_string("    STARTING    ", 1) #PRINT LINE 1
display.lcd_display_string("                ",2) #CLEAN LINE 2
for i in range (16):
    x = '#' * i
    display.lcd_display_string(x, 2) #PRINT LINE 2
    time.sleep(0.2)

display.lcd_display_string("            ",1) #CLEAN LINE 1
display.lcd_display_string("            ",2) #CLEAN LINE 2

GPIO.add_event_detect(ir_sensor, GPIO.RISING, callback=get_rpm)

display.lcd_display_string("SET  : 0 RPM",1) #PRINT LINE 1
display.lcd_display_string("SPEED: 0 RPM",2) #PRINT LINE 2

inpt = float(input("Set RPM: "))
expected = inpt
expected = int(expected)

if inpt == 180:
    speed = 3
    motor.ChangeDutyCycle(speed)
    inpt = -1

elif inpt > 180 and inpt < 400:
    speed = 3
    motor.ChangeDutyCycle(speed)
    inpt = -1

elif inpt == 400:
    speed = 4.5
    motor.ChangeDutyCycle(speed)
    inpt = -1

elif inpt > 400 and inpt < 560:
    speed = 4.5
    motor.ChangeDutyCycle(speed)
    inpt = -1

elif inpt == 560:
    speed = 5
    motor.ChangeDutyCycle(speed)
    inpt = -1

elif inpt > 560 and inpt < 1000:
    speed = 5
    motor.ChangeDutyCycle(speed)
    inpt = -1

elif inpt == 1000:
    speed = 7
    motor.ChangeDutyCycle(speed)
    inpt = -1

elif inpt > 1000 and inpt < 1500:
    speed = 7
    motor.ChangeDutyCycle(speed)
    inpt = -1

elif inpt == 1500:
    speed = 9
    motor.ChangeDutyCycle(speed)
    inpt = -1

elif inpt > 1500 and inpt < 2000:
    speed = 9
    motor.ChangeDutyCycle(speed)
    inpt = -1

elif inpt == 2000:
    speed = 11.5
    motor.ChangeDutyCycle(speed)
    inpt = -1

elif inpt > 2000 and inpt < 2500:
    speed = 11.5
    motor.ChangeDutyCycle(speed)
    inpt = -1

elif inpt == 2500:
    speed = 14
    motor.ChangeDutyCycle(speed)
    inpt = -1

elif inpt > 2500 and inpt < 3000:
    speed = 14
    motor.ChangeDutyCycle(speed)
    inpt = -1

elif inpt == 3000:
    speed = 16.65
    motor.ChangeDutyCycle(speed)
    inpt = -1

elif inpt > 3000 and inpt < 3500:
    speed = 16.65
    motor.ChangeDutyCycle(speed)
    inpt = -1

elif inpt == 3500:
    speed = 20
    motor.ChangeDutyCycle(speed)
    inpt = -1

elif inpt > 3500 and inpt < 4000:
    speed = 20
    motor.ChangeDutyCycle(speed)
    inpt = -1

elif inpt == 4000:
    speed = 23.62
    motor.ChangeDutyCycle(speed)
    inpt = -1

elif inpt > 4000 and inpt < 4500:
    speed = 23.62
    motor.ChangeDutyCycle(speed)
    inpt = -1

elif inpt == 4500:
    speed = 28
    motor.ChangeDutyCycle(speed)
    inpt = -1

elif inpt > 4500 and inpt < 5000:
    speed =28
    motor.ChangeDutyCycle(speed)
    inpt = -1

elif inpt == 5000:
    speed = 33
    motor.ChangeDutyCycle(speed)
    inpt = -1

elif inpt > 5000 and inpt < 5500:
    speed = 33
    motor.ChangeDutyCycle(speed)
    inpt = -1

elif inpt == 5500:
    speed = 38.6
    motor.ChangeDutyCycle(speed)
    inpt = -1

elif inpt > 5500 and inpt < 6000:
    speed = 38.6
    motor.ChangeDutyCycle(speed)
    inpt = -1

elif inpt == 6000:
    speed = 44.9
    motor.ChangeDutyCycle(speed)
    inpt = -1

elif inpt > 6000 and inpt < 6500:
    speed = 44.9
    motor.ChangeDutyCycle(speed)
    inpt = -1

elif inpt == 6500:
    speed = 55
    motor.ChangeDutyCycle(speed)
    inpt = -1

elif inpt > 6500 and inpt < 7000:
    speed = 55
    motor.ChangeDutyCycle(speed)
    inpt = -1

elif inpt == 7000:
    speed = 65
    motor.ChangeDutyCycle(speed)
    inpt = -1

elif inpt > 7000 and inpt < 7200:
    speed = 65
    motor.ChangeDutyCycle(speed)
    inpt = -1

elif inpt == 7200:
    speed = 70
    motor.ChangeDutyCycle(speed)
    inpt = -1

elif inpt == -1:
    print("NOTHING")

try:
    while True:
        display.lcd_display_string("SET  : " + str(expected)+" RPM", 1) #PRINT LINE 1
        display.lcd_display_string("SPEED: " + str(rpm)+" RPM", 2) #PRINT LINE 2

        time.sleep(6)

except KeyboardInterrupt: 
    display.lcd_clear()
    GPIO.cleanup()