from cgitb import text
import time
import os
import glob
import threading
#Detta skript behöver en variabel där man skriver in de olika variablarna för thermometer utdatan. Dessutom behöver man klona "read_temp_raw för att gära att den äver fungerar med temp 2

base_dir = "/sys/bus/w1/devices"

def read_temp_raw():
        text = open("Thermo1.txt")
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
                temp__string2 =lines[1][equal_pos+2:]
                return float(temp__string2)/1000



print(read_temp2())
