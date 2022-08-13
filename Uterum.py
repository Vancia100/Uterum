import time
import threading
import Thermometer
import GPIO


Toltemp = 20, 22 #Mellan dessa 2 värden är där man försöker att hålla temperaturen, där fläktarna inte kommer att köra.
Agrev = 25 #är skilnaden i tempreatur mellan när man ska köra 100% och 20%.
Dif = 20  #är skilnaden i temperatur mellan inne och ute som behövs för att fläktarna ska gå hälften så långsamt, är för närvarande inte implementerat.

FanAuto = False
FanOn = False

def Fan(hastighet):
        if hastighet > 100:
                GPIO.PWM(100) #Kommer ej ihåg om det här är det faktiskt skriptet.
        elif  hastighet > 20:
                GPIO.PWM(20)
        else:
                GPIO.PWM(hastighet)
        #Funktion för att sätta fläkthastigheten

def Buttons():
        while True:
                if GPIO.Button == True:
                        FanOnChange()
                        while GPIO.Button == True:
                                time.sleep(0.5)

                elif GPIO.Button2 == True and FanAuto == False:
                        FanAutoChange()
                        while GPIO.Button2 == True:
                                time.sleep(0.5)
                else:
                        time.sleep(0.2)
def FanAutoChange():
        global FanAuto
        if FanAuto == True:
                FanAuto = False
                if FanOn == True:
                        Fan(100)
                else:
                        Fan(0)
        elif FanAuto == False:
                FanAuto == True
                StartAuto()
#Dessa funktioner kan bli kallade från ett potentiellt annat script där man då kan ändra dessa.
def FanOnChange():
        global FanOn
        if FanOn == False:
                FanOn = True
                Fan(100)
        if FanOn == True:
                FanOn = True
                Fan(0)
def CheckFan():
        global FanAuto, FanOn
        return(FanAuto, FanOn)

def FanAutoSys():
        while True:
                UteTemp = Thermometer.read_temp()
                IneTemp = Thermometer.read_temp2()
                if not(Toltemp[0] <= IneTemp <= Toltemp[1]) and ((IneTemp > UteTemp and IneTemp > Toltemp[1]) or (IneTemp > UteTemp and IneTemp < Toltemp[0])):
                        Fan(round(Agrev*abs(IneTemp-(sum(Toltemp)/2))/(abs(IneTemp-UteTemp)*(1/Dif+1))))
                        time.sleep(1)
                else:
                        time.sleep(1)
                if FanAuto == False:
                        break

def StartAuto():
        T2 = threading.Thread(target=FanAutoSys)
        T2.start()           


#Det som står under main är det som kommer få den att göra coola saker.
def main():
        GPIO.cleanupp()
        GPIO.setmode(GPIO.BCM)
        T1 = threading.Thread(target=Buttons)
        T1.start()
        StartAuto()
if __name__ == "__main__":
        main()
