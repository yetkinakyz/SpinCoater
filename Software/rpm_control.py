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
t = 0
inpt = -1

check = False

sampleRpmList = [ 100, 200, 300, 400, 500, 800,
            1000, 1200, 1500, 1800,
            2000, 2200, 2500, 2800,
            3000, 3200, 3500, 3800,
            4000, 4200, 4500, 4800,
            5000, 5200, 5500, 5800,
            6000, 6200, 6500, 6800,
            7000, 7200]

sampleSpeedList = [   2.8, 3.3, 3.8, 4.2, 4.7, 6,
                6.7, 7.5, 8.5, 10,
                10.5, 11.5, 13, 14.5,
                15.5, 16.8, 18.5, 20,
                21.5, 23, 25, 27.5,
                30, 32, 35.5, 38,
                40.5, 44.0, 48.0, 53.0,
                55.5, 60.5]

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

    elif (n > 25):
        speed = speed + 0.1
        motor.ChangeDutyCycle(speed)

        print("LOW")

    elif (n < -25):
        speed = speed - 0.1
        motor.ChangeDutyCycle(speed)

        print("HIGH")

    else:
        check = True
        print("NEUTRAL")
        
# GET RPM
def get_rpm(c):
    global count
    global sample

    global expected
    global rpm

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

GPIO.add_event_detect(ir_sensor, GPIO.RISING, callback=get_rpm)

print("Welcome!\n")

display.lcd_display_string("  SPIN  COATER  ", 1) #PRINT LINE 1
display.lcd_display_string(" RPM CONTROLLER ", 2) #PRINT LINE 2
time.sleep(1)

display.lcd_display_string("       BY       ", 1) #PRINT LINE 1
display.lcd_display_string("  YETKIN AKYUZ  ", 2) #PRINT LINE 2
time.sleep(1)

display.lcd_display_string("    STARTING    ", 1) #PRINT LINE 1
display.lcd_display_string("                ",2) #CLEAN LINE 2
for i in range (16):
    x = '#' * i
    display.lcd_display_string(x, 2) #PRINT LINE 2
    time.sleep(0.1)

display.lcd_clear()

display.lcd_display_string("SET:    " + str(0) + " SEC",1) #PRINT LINE 1
display.lcd_display_string("        " + str(0) +" RPM",2) #PRINT LINE 2

inpt = float(input("Set RPM: "))

expected = inpt
expected = int(expected)

display.lcd_clear()
display.lcd_display_string("  SPEED  VALUE  ",1) #PRINT LINE 1
display.lcd_display_string(" SET: " + str(expected) + " RPM ",2) #PRINT LINE 2

time.sleep(1)

display.lcd_clear()
display.lcd_display_string("SET:    " + str(t) + " SEC",1) #PRINT LINE 1
display.lcd_display_string("        " + str(expected) + " RPM",2) #PRINT LINE 2

t = int(input("Set Time (sec): "))

display.lcd_clear()
display.lcd_display_string("   TIME  VALUE  ",1) #PRINT LINE 1
display.lcd_display_string(" SET: " + str(t) + " SEC ",2) #PRINT LINE 2

time.sleep(1)

display.lcd_clear()
display.lcd_display_string("SET:    " + str(t) + " SEC",1) #PRINT LINE 1
display.lcd_display_string("        " + str(expected) +" RPM",2) #PRINT LINE 2

time.sleep(2)

display.lcd_clear()
display.lcd_display_string("    MOTOR IS    ",1) #PRINT LINE 1
display.lcd_display_string("  ACCELERATING  ",2) #PRINT LINE 1

for i in sampleRpmList:
    if (expected >= sampleRpmList(i) - 100) and (expected <= sampleRpmList(i) + 100):
        
        print("\ngetRPM=" + str(sampleRpmList(i)))
        print("\ngetSpeed=" + str(sampleSpeedList(i))+"\n")

        motor.ChangeDutyCycle(sampleSpeedList(i))
    else:
        continue

try:
    while True:
        if check == False:
            print("ACCELERATING...")
            time.sleep(1)
            
        else:

            print("ACCELERATED!")
            
            t_end = t

            while t_end > 0:
                
                display.lcd_clear()
                display.lcd_display_string("TIME : " + str(t_end)+" SEC", 1) #PRINT LINE 1
                display.lcd_display_string("SPEED: " + str(rpm)+" RPM", 2) #PRINT LINE 2

                time.sleep(1)
                t_end = t_end - 1

            display.lcd_clear()
            display.lcd_display_string("      DONE      ",1) #PRINT LINE 1

            break

except KeyboardInterrupt: 
    GPIO.cleanup()