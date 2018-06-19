from RPi.GPIO import *
from time import sleep

mr1=16 # right motor, num 1
mr2=20 # right motor, num 2
ml1=19 # left motor, num 1
ml2=26 # left motor, num 2
srm=12 # right IR sensor
slm=6  # left  IR sensor
bt=1 # back time, how much sec comeback to turn again

# setmode and setup GPIOs
setmode(BCM)
setup(slm, IN)
setup(srm, IN)
setup(mr1, OUT)
setup(mr2, OUT)
setup(ml1, OUT)
setup(ml2, OUT)


def sr(): # right IR senson function
    if input(srm)==1:
        print('nothing is not in right side')
    if input(srm)==0:
        print('something found on right side')
    return input(srm)

def sl():
    if input(slm)==1:
        print('nothing is not in left side')
    if input(slm)==0:
        print('something found on left side')
    return input(slm)

def mr(c): # controle right motor, 0=stop, 1=go, -1=back
    if c==0:
        output(mr1, 0)
        output(mr2, 0)
    if c==1:
        output(mr1, 1)
        output(mr2, 0)
    if c==(-1):
        output(mr1, 0)
        output(mr2, 1)

def ml(c): # controle right motor, 0=stop, 1=go, -1=back
    if c==0:
        output(ml1, 0)
        output(ml2, 0)
    if c==1:
        output(ml1, 1)
        output(ml2, 0)
    if c==(-1):
        output(ml1, 0)
        output(ml2, 1)

def move(d, t): # use ml() and mr() function for move
    if d==0: # stop
        mr(0)
        ml(0)
    if d==1: # move forward
        mr(1)
        ml(1)
    if d==2: # turn right, normal mode
        mr(0)
        ml(1)
    if d==3: # turn left,  normal mode
        mr(1)
        ml(0)
    if d==4: # turn right, fast mode
        mr(-1)
        ml(1)
    if d==5: # turn left,  fast mode
        mr(1)
        ml(-1)
    if d==(-1): # move backward
        mr(-1)
        ml(-1)
    if d==(-2): # move backward, turn to the right
        mr(0)
        me(-1)
    if d==(-3): # move backward, turn to the left
        mr(-1)
        ml(0)
    if d==(-4): # move backward, turn to the right, fast mode
        mr(1)
        ml(-1)
    if d==(-5): # move backward, turn to the left,  fast mode
        mr(-1)
        ml(1)
    sleep(t)



while True:
    if sr()==1: # if right sensor detected something, get back and turn to the left
        move(-1, bt)
        move(3)
    if sl()==1: # if left  sensor detected something, get back and turn to the right
        move(-1, bt)
        move(2)
    if sl()==0 and sr()==0: # if nothing wasn't on front of the but, keep going
        move(1, 0)

