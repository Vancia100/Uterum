PINnr = {}
class PWM:
    global ON
    global duty_cycle
    def __init__(self, channel, frequenzy) -> None:
        self.channel = channel
        self.frequenzy = frequenzy
    def start(DC = None):
        if DC != None:
            duty_cycle = DC
        ON = True
        print(f"Starting with a duty cycle at {duty_cycle} and frequenzy of ?")
    def ChangeDutyCycle(DC = None):
        if DC != None:
            duty_cycle = DC
            print(f"Duty cycle is now at {DC}")
    def stop():
        ON = False
        print(f"PWM turned of")
        



def CheckBackGround(Dictionary, Mode):
    if PINnr.get(Dictionary[0]) == Mode:
        return True
    else:
        return False

#simple setup finctions
def BCM():
    return("BCM")
def BOARD():
    return("BOARD")
def cleanup():
    print("Cleanup Complete!")
    PINnr = {}
def setmode(Mode):
    print("Rpi is now in " + str(Mode) + " mode")

#Setup a pin to a value:
def setup(Pin, Mode, Value = None):
    if Value != None:
        print(f'pin nr:{Pin} is set up in {Mode} mode and has the value {Value}')
        PINnr[Pin] = [Mode, Value]
    else:
        print(f'pin nr:{Pin} is set up in {Mode} mode.')
        PINnr[Pin] = [Mode]
#The posible values:
def OUT():
    return("OUT")
def IN():
    return("IN")

def HIGH():
    return("HIGH")
def LOW():
    return("LOW")

"""
Some sample code from actual code.

GPIO.cleanup()
GPIO.setmode(BCM)
GPIO.setmode(BOARD)

GPIO.setup(18,OUT, HIGH) TODO Look up how this syntax actualy looks and implemnt it accordingly.
"""