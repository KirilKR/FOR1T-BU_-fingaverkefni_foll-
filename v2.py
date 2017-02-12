#Kiril Krushkov
#1.2.2017
#Æfingaverkefni 1-2 - Föll

#Whole chapter:
def reiknaRummalKulu():
    radius = int(input("Sláðu inn radíus fyrir hringinn "))
    rummalKulu = (4*3.14*radius)/3
    print(rummalKulu)
reiknaRummalKulu()
def reiknaRummalKassa():
    lengd = int(input("Sláðu inn lengd kassans "))
    breidd = int(input("Sláðu inn breidd kassans "))
    hæd = int(input("Sláðu inn hæð kassans "))
    rummalKassa = lengd*breidd*hæd
    print(rummalKassa)
reiknaRummalKassa()
def reiknaFlatarmalTrihyrnings():
    breidd = int(input("Sláðu inn breidd þríhyrningsins "))
    hæd = int(input("Sláðu inn hæð þríhyrningsins "))
    flatarmalTrihyrnings = breidd*hæd
    print(flatarmalTrihyrnings)
reiknaFlatarmalTrihyrnings()