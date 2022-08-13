from pickle import APPEND
from statistics import mode
import time

PINnr = []

def BCM():
    return("BCM")
def BOARD():
    return("Board")
def cleanupp():
    print("CleanupComplete!")
def setmode(Mode):
    print("Rpi är nu i " + str(Mode) + " läget")
def setup(Pin, Mode):
    print(f'pin nr:{Pin} is set up in {Mode} mode.')
    PINnr.append(Pin, Mode)

def OUT():
    return("OUT")
def IN():
    return("IN")
def PWM():
    print("PWM")
def HIGH():
    return("HIGH")
def LOW():
    return("LOW")


def output(Pin, HiLo):
    if (Pin, "OUT") in PINnr:
        print(f'Outputting {HiLo} on pin {Pin}')
    else:
        print("Pin not setup correctly")



def Button():
    return(bool(input("is the button pressed? (True or False)")))

def Button2():
    return(bool(input("is the button pressed? (True or False)")))