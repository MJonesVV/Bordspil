from machine import *
from random import *
from time import *
#Hvað ljós er hvað
Ljos_TopLeft = Pin(12, Pin.OUT)
Ljos_Left = Pin(11, Pin.OUT)
Ljos_BotLeft = Pin(10, Pin.OUT)
Ljos_Mid = Pin(18, Pin.OUT)
Ljos_TopRight = Pin(17, Pin.OUT)
Ljos_Right = Pin(16, Pin.OUT)
Ljos_BotRight = Pin(15, Pin.OUT)
#Hljóð og takki og reed
takki = Pin(13,Pin.IN,Pin.PULL_UP)
Hljod = PWM(Pin(21))
Reed = Pin(2,Pin.IN,Pin.PULL_UP)
#notur fyrir buzzer
tones = {
"B0": 31,"C1": 33,"CS1": 35,"D1": 37,"DS1": 39,"E1": 41,"F1": 44,"FS1": 46,
"G1": 49,"GS1": 52,"A1": 55,"AS1": 58,"B1": 62,"C2": 65,
"CS2": 69,"D2": 73,"DS2": 78,"E2": 82,"F2": 87,"FS2": 93,"G2": 98,
"GS2": 104,"A2": 110,"AS2": 117,"B2": 123,"C3": 131,"CS3": 139,
"D3": 147,"DS3": 156,"E3": 165,"F3": 175,"FS3": 185,
"G3": 196,"GS3": 208,"A3": 220,"AS3": 233,"B3": 247,"C4": 262,"CS4": 277,"D4": 294,"DS4": 311,
"E4": 330,"F4": 349,"FS4": 370,"G4": 392,"GS4": 415,"A4": 440,"AS4": 466,"B4": 494,"C5": 523,"CS5": 554,"D5": 587,"DS5": 622,"E5": 659,"F5": 698,
"FS5": 740,"G5": 784,"GS5": 831,"A5": 880,"AS5": 932,"B5": 988,"C6": 1047,"CS6": 1109,"D6": 1175,"DS6": 1245,"E6": 1319,"F6": 1397,"FS6": 1480,"G6": 1568,"GS6": 1661,
"A6": 1760,"AS6": 1865,"B6": 1976,"C7": 2093,"CS7": 2217,"D7": 2349,"DS7": 2489,"E7": 2637,"F7": 2794,"FS7": 2960,"G7": 3136,"GS7": 3322,"A7": 3520,
"AS7": 3729,"B7": 3951,"C8": 4186,"CS8": 4435,"D8": 4699,"DS8": 4978
}
#Tónlist
kastad = ["AS6", 0, 0, "B6",0, "C7", 0, 0, "A6", 0, "E7"]
victory = ["DS6",0, 0 ,"G6",0, 0,"C7",0, 0,"D7", 0,"AS6", 0,"C7",0,"A6", 0,0,"F6", 0 ,0, "G6", 0,0,0]
#Kóði til þess að tónlist virki, (stolið)
def playtone(frequency):
    Hljod.duty_u16(1000)
    Hljod.freq(frequency)

def bequiet():
    Hljod.duty_u16(0)

def playsong(mysong):
    for i in range(len(mysong)):
        if (mysong[i] == 0 ):
            bequiet()
        else:
            playtone(tones[mysong[i]])
        sleep_ms(150)
    bequiet()

# Define alla hliða á tening
def ten(tala):
        if tala == 1:
            Ljos_Mid.value(1)
        elif tala == 2:
            Ljos_BotLeft.value(1)
            Ljos_TopRight.value(1)
        elif tala == 3:
            Ljos_BotLeft.value(1)
            Ljos_TopRight.value(1)
            Ljos_Mid.value(1)
        elif tala == 4:
            Ljos_BotLeft.value(1)
            Ljos_TopRight.value(1)
            Ljos_BotRight.value(1)
            Ljos_TopLeft.value(1)
        elif tala == 5:
            Ljos_BotLeft.value(1)
            Ljos_TopRight.value(1)
            Ljos_BotRight.value(1)
            Ljos_TopLeft.value(1)
            Ljos_Mid.value(1)
        elif tala == 6:
            Ljos_BotLeft.value(1)
            Ljos_TopRight.value(1)
            Ljos_BotRight.value(1)
            Ljos_TopLeft.value(1)
            Ljos_Right.value(1)
            Ljos_Left.value(1)
        else:
            Ljos_BotLeft.value(0)
            Ljos_TopRight.value(0)
            Ljos_BotRight.value(0)
            Ljos_TopLeft.value(0)
            Ljos_Right.value(0)
            Ljos_Left.value(0)
            Ljos_Mid.value(0)
            
listi = []
#Það sem er í gangi
while True:
    Hljod.duty_u16(0)
    ten(10)
    if takki.value() == 0:
        for i in range(10):
            tala = randint(1,6)
            listi.append(tala)
        for tala in listi:
            ten(tala)
            sleep_ms(200)
            ten(10)
        listi.clear()
        kast = randint(1,6)
        ten(kast)
        playsong(kastad)
        sleep_ms(2000)
    if Reed.value():
        Ljos_BotLeft.value(0)
        Ljos_TopRight.value(0)
        Ljos_BotRight.value(0)
        Ljos_TopLeft.value(0)
        Ljos_Right.value(0)
        Ljos_Left.value(0)
        Ljos_Mid.value(0)
    else:
        Ljos_BotLeft.value(1)
        Ljos_TopRight.value(1)
        Ljos_BotRight.value(1)
        Ljos_TopLeft.value(1)
        Ljos_Right.value(1)
        Ljos_Left.value(1)
        Ljos_Mid.value(1)
        playsong(victory)



        

    
