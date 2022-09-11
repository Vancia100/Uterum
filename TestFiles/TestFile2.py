import random

#TODO make readLInnear actually work! no clue what is wrong.


Instance = 0

def readTemp():
    global Instance, Start, Expo
    if Instance == 0:
        Instance = 1
        Expo = random.random()
        Start = random.randint(15,25)
        print(f'The temp is contolled exponentioaly, \n With a starting value of {Start} and a exponent of {round(Expo/4, 2)}!')
        return(None)
    else:
        Instance += 0.05
        return(float(round( Start*(Expo+1)**(Instance/4), 2)))

def readLinnear():
    global Instance, Start, Expo
    if Instance == 0:
        Instance == 1
        Expo = random.random()
        Start = random.randint(15,25)
        print(f'The temp is contolled linnearly, \n With a starting value of {Start} and a K value of {round(Expo/4, 2)}!')
        return(None)
    else:
        return(float(round(Instance*(Expo/4)+ Start)))
    