from machine import Pin
import time
import random
led1 = Pin(7, Pin.OUT)
led2 = Pin(8, Pin.OUT)
led3 = Pin(9, Pin.OUT)
led4 = Pin(10, Pin.OUT)
led5 = Pin(11, Pin.OUT)
led6 = Pin(12, Pin.OUT)

button1 = Pin(3, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(4, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(5, Pin.IN, Pin.PULL_DOWN)
button4 = Pin(6, Pin.IN, Pin.PULL_DOWN)
button5 = Pin(2, Pin.IN, Pin.PULL_DOWN)

time_s = 0
time_e = 0
reaction_time = 0

def restart():
    global light_num
    print('restart')
    if light_num == 1:
        led1.toggle()
    if light_num == 2:
        led2.toggle()
    if light_num == 3:
        led3.toggle()
    if light_num == 4:
        led4.toggle()
    light_num = 0


while True:
    light_num = random.randint(1,4)
    time_e = time.time()
    
    if light_num == 1:
        led1.toggle()
    if light_num == 2:
        led2.toggle()
    if light_num == 3:
        led3.toggle()
    if light_num == 4:
        led4.toggle()
    time_s = time.time()
        
    while light_num == 1:
        if button1.value():
            led1.toggle()
            time.sleep(0.1)
            light_num = 0
            time_e = time.time()
        if button5.value():
            restart()
        
    while light_num == 2:
        if button2.value():
            led2.toggle()
            time.sleep(0.1)
            light_num = 0
            time_e = time.time()
        if button5.value():
            restart()
        
    while light_num == 3:
        if button3.value():
            led3.toggle()
            time.sleep(0.1)
            light_num = 0
            time_e = time.time()
        if button5.value():
            restart()
        
    while light_num == 4:
        if button4.value():
            led4.toggle()
            time.sleep(0.1)
            light_num = 0
            time_e = time.time()
        if button5.value():
            restart()
            
    reaction_time = time_e - time_s
    
    if reaction_time > 1:
        led6.toggle()
        time.sleep(0.3)
        led6.toggle()
    else:
        led5.toggle()
        time.sleep(0.3)
        led5.toggle()
        
    print(reaction_time)


        
