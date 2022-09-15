import json
from tkinter.ttk import Separator

def FileRaw(Value = None):
    with open("TestFiles/Jim.json", "r+") as fake:
        if Value != None:
            fake.write(json.dumps(Value, indent=2))
        else:
            return(json.loads(fake.read()))


def main():
    Inp = input("Skirv in värde:")
    yes = FileRaw()
    if not(Inp):
        print(yes)
    else:
        try:
            print(yes[Inp])
        except KeyError:
            yes[Inp] = (input(f"Nytt sökvärde skriv skriv nytt värde för {Inp}: "))
            FileRaw(yes)

if __name__ == "__main__":
    pass
    main()
    #test()