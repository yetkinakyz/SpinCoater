"""
SPIN COATER SPEED TEST SOFTWARE
                by Yetkin AKYUZ

        Website: https://yetkinakyuz.com
        Email:   contact@yetkinakyuz.com
""" 

##### LIBRARIES #####
import RPi.GPIO as GPIO #RASPBERRY PI GPIO LIBRARY WIKI: https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/
import RPi_I2C_driver #LCD I2C LIBRARY
import time

##### SETUP ##### 
# MOTOR
motor_in3 = 23
motor_in4 = 24
motor_en = 25

speed = 15
motor_temp1 = 1

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(motor_in3,GPIO.OUT)
GPIO.setup(motor_in4,GPIO.OUT)
GPIO.setup(motor_en,GPIO.OUT)
GPIO.output(motor_in3,GPIO.LOW)
GPIO.output(motor_in4,GPIO.LOW)

motor=GPIO.PWM(motor_en,1000)
motor.start(15)

# IR SENSOR
ir_sensor = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(ir_sensor,GPIO.IN)

sample = 120
count = 0

start = 0
end = 0

 ##### MODULES #####
 # SET START TIME
def set_start():
 	global start
 	start = time.time()

#SET END TIME
def set_end(): 
        global end
        end = time.time()

# GET RPM
def get_rpm(c): 
    global count

    if count == 0:
            set_start()        
            count = count + 1
    else:
            count = count + 1
            
    if count == sample:
            set_end()

            delta = end - start #TIME OF A 360 DEGREES ROTATION OF MOTOR DISK
            delta = delta / 60

            rpm = round((sample / delta)/2)

            RPi_I2C_driver.lcd().lcd_display_string(str(rpm)+" RPM",2) #PRINT LINE 2

            count = 0

# MESSAGES
print("\n============================================================")
print("    SPIN COATER MOTOR SPEED TESTER v1.0 BY YETKIN AKYUZ")
print("============================================================")
print("                    COMMAND LIST\n")
print("Run:\t'run'")
print("Stop:\t'stop'")
print("Speed:\t'speed'")
print("Rotation:\t'f'(Forward) or 'b'(Backward)")
print("Help:\t'help'")
print("Exit:\t'exit'\n")

# LCD MESSAGE
RPi_I2C_driver.lcd().lcd_display_string("MOTOR SPEED TEST",1)  #PRINT LINE 1

# EXECUTE get_rpm MODULE IF IR_SENSOR CAPTURES ANY CHANGE OF MOTOR SPEED
GPIO.add_event_detect(ir_sensor, GPIO.FALLING, callback=get_rpm)

try:
    while True:
        option = raw_input("\nCommand : ") #INPUT FROM KEYBOARD

        #FOR MOTOR SPEED RATE
        if option == "speed":
            speed = float(raw_input("\nSpeed Rate (1-100): ")) #INPUT FROM KEYBOARD

            #MOTOR SPEED VALUE MUST BE BETWEEN 1 AND 100
            if speed >= 0.0 and speed <= 100.0:
                print("[  i  ] Speed: " + str(speed))
                print(" ") 
                motor.ChangeDutyCycle(speed)

            else:
                print("[  !  ] Error: Speed value must be 1-100")
                print("[  i  ] Type help to see command list.")

        #FOR FORWARD ROTATION
        elif option == "f":
            motor_temp1=1

            print("[  i  ] Rotation: Forward")
            print(" ") 

        #FOR BACKWARD ROTATION
        elif option == "b": 
            motor_temp1=0

            print("[  i  ] Rotation: Backward")
            print(" ")           

        #RUNS MOTOR
        elif option == "run": 
            if not speed:
                print("[  !  ] Error: Rotation info not found.")
                print("[  i  ] Type help to see command list.")

            else:
                #FOR FORWARD ROTATION
                if motor_temp1 == 1: 
                    GPIO.output(motor_in3,GPIO.HIGH)
                    GPIO.output(motor_in4,GPIO.LOW)

                #FOR BACKWARD ROTATION
                elif motor_temp1 == 0: 
                    GPIO.output(motor_in3,GPIO.LOW)
                    GPIO.output(motor_in4,GPIO.HIGH)
                
                else:
                    print("[  !  ] Error: Rotation info not found.")
                    print("[  i  ] Type help to see command list.")

        elif option == "stop":
            motor.ChangeDutyCycle(0)
            GPIO.output(motor_in3,GPIO.LOW)
            GPIO.output(motor_in4,GPIO.LOW)

        #HELP COMMAND
        elif option == "help": 
            print(" ")
            print("[  i  ] COMMAND LIST \n")
            print("Run: run")
            print("Stop: stop")  
            print("Speed: 0-100 [Default: 5]")
            print("Rotation: 'f' (Forward) or 'b' (Backward) [Default: Forward]")
            print("Help: 'help'")
            print("Exit: 'exit'")
            print(" ")

        #EXIT COMMAND
        elif option == "exit": 
            RPi_I2C_driver.lcd().lcd_display_string(" ",1)  #CLEAN LINE 1
            break   

        #IF OPTION IS NON OF THEM
        else: 
            print("[  !  ] Error: Command not found.")
            print("[  i  ] Type help to see command list.")
         
except KeyboardInterrupt: 
 	RPi_I2C_driver.lcd().lcd_display_string(" ",1) #CLEAN LINE 1
 	GPIO.cleanup()
