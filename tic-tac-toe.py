from time import sleep
import select
import sys

S1 = input("Spieler1: ")
S2 = input("Spieler2: ")

for i in range(3,0,-1):
    print(i,end="\r")
    sleep(1)

class fields:
    figuren = ["","",S1,S2]
    field = [0,0,0,0,0,1,0,0,0]
    zug = 2
    def figure(f,z):
        l = int(size.width / 3)
        if f == 0:
            for i in range(l):
                print(" ",end="")
        elif f == 1:
            if z > 1 and z < 10:
                for i in range(2):
                    print(" ",end="")
                for i in range(16):
                    print("#",end="")
                for i in range(2):
                    print(" ", end="")
            else:
                for i in range(20):
                    print(" ",end="")
        elif f == 2:
            if z == 1 or z == 10:
                for i in range(20):
                    print(" ",end="")
            elif z == 5:
                for i in range(2):
                    print(" ",end="")
                for i in range(8):
                    print("-",end="")
                print("+",end="")
                for i in range(7):
                    print("-",end="")
                for i in range(2):
                    print(" ",end="")
            else:
                for i in range(10):
                    print(" ",end="")
                print("|",end="")
                for i in range(9):
                    print(" ",end="")
        else:
            if z == 1 or z == 10:
                for i in range(20):
                    print(" ",end="")
            elif z == 2 or z == 9:
                for i in range(2):
                    print(" ",end="")
                print("+", end="")
                for i in range(14):
                    print("-",end="")
                print("+",end="")
                for i in range(2):
                    print(" ",end="")
            else:
                for i in range(2):
                    print(" ",end="")
                print("|", end="")
                for i in range(14):
                    print(" ",end="")
                print("|",end="")
                for i in range(2):
                    print(" ",end="")

class size:
    width = 60
    hight = 30
    def horizontal():
        for a in range(3):
            print("+",end="")
            for i in range(int(size.width / 3)):
                print('-',end="")
        print("+")
    def vertical(v1,v2,v3):
        for i in range(int(size.hight / 3)):
            print("|",end="")
            fields.figure(v1,i+1)
            print("|",end="")
            fields.figure(v2,i+1)
            print("|",end="")
            fields.figure(v3,i+1)
            print("|")
    def respawn(value):
        size.horizontal()
        for i in range(3):
            size.vertical(value[i*3],value[(i*3)+1],value[(i*3)+2])
            size.horizontal()

def count(w):
    f = fields.field
    for i in range(9):
        if f[i] == 1:
            fields.field[i] = w
            c = True
            for a in range(8):
                b = i+a+1
                if b > 8:
                    b -= 9
                if f[b] == 0:
                    fields.field[b] = 1
                    c = False
                    break
            if c == True:
                fields.field[i] = fields.zug
            break
        
def wait_for_enter():
    i, o, e = select.select([sys.stdin], [], [], 1)
    if i:
        input()
        a = fields.zug
        if a == 2:
            fields.zug = 3
        else:
            fields.zug = 2
        return a
    else:
        return 0
    
def Unentschieden():
    c = True
    for i in fields.field:
        if i == 1:
            c = False
    return c

def pruefen(s):
    l = fields.field
    if l[0] == s and l[1] == s and l[2] == s:
        w = True
    elif l[3] == s and l[4] == s and l[5] == s:
        w = True
    elif l[6] == s and l[7] == s and l[8] == s:
        w = True
    elif l[0] == s and l[3] == s and l[6] == s:
        w = True
    elif l[1] == s and l[4] == s and l[7] == s:
        w = True
    elif l[2] == s and l[5] == s and l[8] == s:
        w = True
    elif l[0] == s and l[4] == s and l[8] == s:
        w = True
    elif l[2] == s and l[4] == s and l[6] == s:
        w = True
    else:
        w = False
    return w
a = False
while True:
    x = wait_for_enter()
    count(x)
    for i in range(50):
        print("")
    print(f"{fields.figuren[fields.zug]} ist an der Reihe")
    size.respawn(fields.field)
    u = Unentschieden()
    if x == 2 or x == 3:
        a = pruefen(x)
    if a == True:
        print(f"{fields.figuren[x]} hat Gewonnen!")
        break
    if u == True:
        print("Unentschieden!")
        break
