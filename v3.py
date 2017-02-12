#Kiril Krushkov
#1.2.2017
#Æfingaverkefni 1-3 - Föll

#Whole chapter "Unfinished":
listi = []
for x in range(5):
    tala = int(input("Sláðu inn tölu"))
    listi.append(tala)

def skrifaUt(listi):
    print(listi)
def stærsta(listi):
    stor = listi[0]
    for tala in listi:
        if tala > stor:
            stor = tala
    return stor

def minnsta(listi):
    litill = listi[0]
    for tala in listi:
        if litill < listi:
            litill = tala
    return litill

def summa(listi):
    print("stuff")