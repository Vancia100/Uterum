from time import sleep
#import TestFile2
from TestFile2 import readTemp as getValue # does not work with readLinnear


TempTime = []
Language = True #True for Exponetion false for linnear

#Driver fram ett budget "I"
#def getValue():
#    if Language:
#        return(float(TestFile2.readTemp()))
#    else: 
#        return(float(TestFile2.readLinnear()))

def PID():
    while True:
        Temp1 = getValue()
        if Temp1 != None:
            TempTime.append(Temp1)
            if len(TempTime) > 60:
                TempTime.remove(TempTime[0])
            print(TempTime)
            print(round(Temp1 - sum(TempTime)/len(TempTime), 2))
        sleep(2)

def main():
    PID()
if __name__ == "__main__":
    (main())