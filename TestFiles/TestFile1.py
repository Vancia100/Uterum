from time import sleep

TrueOrFalse = False
print("True Or false exists here!")

def change():
    global TrueOrFalse
    if TrueOrFalse == True:
        TrueOrFalse = False
    elif TrueOrFalse == False:
        TrueOrFalse = True



while True:
    print(TrueOrFalse)
    sleep(1)

        

