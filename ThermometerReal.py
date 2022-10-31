import time
import os
import glob
import threading

base_dir = "/sys/bus/w1/devices" #Where you find the files for 1w on RPI.
#Update as needed.
#TODO Make 2nd thermometer

def read_temp_raw():
        text = open(base_dir+"/28-3c76f648ef1e/w1_slave")
        lines = text.readlines()
        text.close
        return lines


def read_temp_raw2():
        text = open("Thermo2.txt")
        lines = text.readlines()
        text.close
        return lines


def read_temp():
        lines = read_temp_raw()
        while lines[0].strip()[-3:] != "YES":
                time.sleep(3)
                lines = read_temp_raw()
        equal_pos = lines[1].find("t=")
        if equal_pos != -1:
                
                temp_string = lines[1][equal_pos+2:]
                return float(temp_string)/1000


def read_temp2():
        lines = read_temp_raw2()
        while lines[0].strip()[-3:] != "YES":
                time.sleep(3)
                lines = read_temp_raw2
        equal_pos = lines[1].find("t=")
        if equal_pos != -1:
                temp__string =lines[1][equal_pos+2:]
                return float(temp__string)/1000



#This is not the main script but just a way of testing if the thermometer is working properly.
#If you want to test the thermometer lanch this script, otherwise this code will lay dormant.
def main():
        while True:
            print(read_temp())
            #print(read_temp2())
            time.sleep(1)
if __name__ == "__main__":
        main()

