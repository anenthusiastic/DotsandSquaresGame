harfler = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T"]

player1 = str.capitalize(input("1. oyuncuyu temsilen bir karakter giriniz : "))
player2 =str.capitalize(input("2. oyuncuyu temsilen bir karakter giriniz : "))
while(player1 == player2):
    player2 = str.capitalize(input("Aynı karakter olmamalı ! 2. oyuncuyu temsilen bir karakter giriniz : "))

satır = int(input("satır sayısını giriniz (3-7): "))
while (satır < 3 or satır> 7):
    satır = int(input("Yanlış giriş ! satır sayısını giriniz (3-7): "))

sütun = int(input("sütun sayısını giriniz (3-19) : "))
while (sütun < 3 or sütun > 19):
    sütun = int(input("Yanlış giriş ! sütun sayısını giriniz (3-19) : "))

satırlar = []
sütunlar = []
players = []
for i in range(satır + 1):
    dizi = []
    for j in range(sütun):
        if(i==0 or i== satır):
            dizi.append("_ _ _ ")
        else:
            dizi.append("      ")

    satırlar.append(dizi)

for i in range(satır * 3):
    dizi = []
    for j in range(sütun + 1):
        if(j==0 or j==sütun):
            dizi.append("|")
        else:
            dizi.append(" ")
    sütunlar.append(dizi)

for i in range(satır):
    dizi = []
    for i in range(sütun):
        dizi.append(" ")
    players.append(dizi)

def oyunAlanı():
    ilksatır = []
    for i in range (sütun*6):
        ilksatır.append(" ")
    for i in range(sütun):
        ilksatır[3+6*i] = harfler[i]

    print(" ",end="")
    for i in ilksatır:
        print(i,end="")

    print()

    print("  ",end="")
    for i in satırlar[0]:
        print(i,end="")

    print()

    for i in range (satır*3):
        if(i%3 != 1):
            print(" ",end="")
        else:
            print(int((i-1)/3)+1,end="")
        for j in range(sütun+1)    :
            if(j!=sütun):
                if(i%3 == 1):
                    print(sütunlar[i][j] + 2* " "+players[int((i-1)/3)][j]+2*" ", end="")
                else:
                    print(sütunlar[i][j] + 5 * " ",end="")
            else:
                print(sütunlar[i][j])
        if(i%3==2) :
            print("  ",end="")
            for k  in range (sütun):
                if(k!= sütun-1):
                    print(satırlar[int((i+1)/3)][k],end="")
                else:
                    print(satırlar[int((i + 1) / 3)][k])

def oyunDevam():
    for i in range(satır+1):
        for j in range(sütun):
            if(satırlar[i][j] == "      "):
                return True
    for i in range(satır*3):
        for j in range(sütun+1):
            if(sütunlar[i][j] == " "):
                return True
    return False

sıra = player1

while(oyunDevam()):
    oyunAlanı()
    girdi = ""
    if(sıra == player1):
        girdi = input("Oyuncu 1 için girdi bekleniyor (Örnek : 1AD) : ")
    if (sıra == player2):
        girdi = input("Oyuncu 2 için girdi bekleniyor (Örnek : 1AD) : ")
    while((girdi[0] not in ["1","2","3","4","5","6","7"]) or (int(girdi[0])>satır) or (girdi[1] not in harfler[0:sütun]) or (
        girdi[2] not in ["B","D","K","G"]) or (len(girdi)!=3)):
        girdi = input("Hatalı giriş yapıldı ! Tekrar giriniz : ")

    if (girdi[2] == "B" and sütunlar[(int(girdi[0]) - 1) * 3][harfler.index(girdi[1])] == " "):
        sütunlar[(int(girdi[0]) - 1) * 3][harfler.index(girdi[1])] = "|"
        sütunlar[(int(girdi[0]) - 1) * 3 + 1][harfler.index(girdi[1])] = "|"
        sütunlar[(int(girdi[0]) - 1) * 3 + 2][harfler.index(girdi[1])] = "|"

    elif (girdi[2] == "D" and sütunlar[(int(girdi[0]) - 1) * 3][harfler.index(girdi[1]) + 1] == " "):
        sütunlar[(int(girdi[0]) - 1) * 3][harfler.index(girdi[1]) + 1] = "|"
        sütunlar[(int(girdi[0]) - 1) * 3 + 1][harfler.index(girdi[1]) + 1] = "|"
        sütunlar[(int(girdi[0]) - 1) * 3 + 2][harfler.index(girdi[1]) + 1] = "|"

    elif (girdi[2] == "K" and satırlar[int(girdi[0]) - 1][harfler.index(girdi[1])] == "      "):
        satırlar[int(girdi[0]) - 1][harfler.index(girdi[1])] = "_ _ _ "

    elif (girdi[2] == "G" and satırlar[int(girdi[0])][harfler.index(girdi[1])] == "      "):
        satırlar[int(girdi[0])][harfler.index(girdi[1])] = "_ _ _ "

    else:
        print("Çizdirmek istediğiniz yer dolu !")
        continue

    kareTamamlandı = False

    if (girdi[2] == "B"):
        if ((sütunlar[(int(girdi[0]) - 1) * 3][harfler.index(girdi[1]) - 1] == "|") and (
                    satırlar[int(girdi[0]) - 1][harfler.index(girdi[1]) - 1] == "_ _ _ ") and (
                    satırlar[int(girdi[0])][harfler.index(girdi[1]) - 1] == "_ _ _ ")):
            players[int(girdi[0]) - 1][harfler.index(girdi[1]) - 1] = sıra
            kareTamamlandı = True

        if ((sütunlar[(int(girdi[0]) - 1) * 3][harfler.index(girdi[1]) + 1] == "|") and (
                    satırlar[int(girdi[0]) - 1][harfler.index(girdi[1])] == "_ _ _ ") and (
                    satırlar[int(girdi[0])][harfler.index(girdi[1])] == "_ _ _ ")):
            players[int(girdi[0]) - 1][harfler.index(girdi[1])] = sıra
            kareTamamlandı = True

    if (girdi[2] == "D"):
        if ((sütunlar[(int(girdi[0]) - 1) * 3][harfler.index(girdi[1])] == "|") and (
                    satırlar[int(girdi[0]) - 1][harfler.index(girdi[1])] == "_ _ _ ") and (
                    satırlar[int(girdi[0])][harfler.index(girdi[1])] == "_ _ _ ")):
            players[int(girdi[0]) - 1][harfler.index(girdi[1])] = sıra
            kareTamamlandı = True

        if ((sütunlar[(int(girdi[0]) - 1) * 3][harfler.index(girdi[1]) + 2] == "|") and (
                    satırlar[int(girdi[0]) - 1][harfler.index(girdi[1]) + 1] == "_ _ _ ") and (
                    satırlar[int(girdi[0])][harfler.index(girdi[1]) + 1] == "_ _ _ ")):
            players[int(girdi[0]) - 1][harfler.index(girdi[1]) + 1] = sıra
            kareTamamlandı = True

    if (girdi[2] == "K"):
        if ((satırlar[int(girdi[0]) - 2][harfler.index(girdi[1])] == "_ _ _ ") and (
                    sütunlar[(int(girdi[0]) - 2) * 3][harfler.index(girdi[1])] == "|") and (
                    sütunlar[(int(girdi[0]) - 2) * 3][harfler.index(girdi[1]) + 1] == "|")):
            players[int(girdi[0]) - 2][harfler.index(girdi[1])] = sıra
            kareTamamlandı = True

        if ((satırlar[int(girdi[0])][harfler.index(girdi[1])] == "_ _ _ ") and (
                    sütunlar[(int(girdi[0]) - 1) * 3][harfler.index(girdi[1])] == "|") and (
                    sütunlar[(int(girdi[0]) - 1) * 3][harfler.index(girdi[1]) + 1] == "|")):
            players[int(girdi[0]) - 1][harfler.index(girdi[1])] = sıra
            kareTamamlandı = True

    if (girdi[2] == "G"):
        if ((satırlar[int(girdi[0]) - 1][harfler.index(girdi[1])] == "_ _ _ ") and (
                    sütunlar[(int(girdi[0]) - 1) * 3][harfler.index(girdi[1])] == "|") and (
                    sütunlar[(int(girdi[0]) - 1) * 3][harfler.index(girdi[1]) + 1] == "|")):
            players[int(girdi[0]) - 1][harfler.index(girdi[1])] = sıra
            kareTamamlandı = True

        if ((satırlar[int(girdi[0]) + 1][harfler.index(girdi[1])] == "_ _ _ ") and (
                    sütunlar[(int(girdi[0])) * 3][harfler.index(girdi[1])] == "|") and (
                    sütunlar[(int(girdi[0])) * 3][harfler.index(girdi[1]) + 1] == "|")):
            players[int(girdi[0])][harfler.index(girdi[1])] = sıra
            kareTamamlandı = True

    if(not kareTamamlandı):
        if(sıra == player2):
            sıra = player1
        else:
            sıra = player2

oyunAlanı()

sayac1 = 0
sayac2 = 0
for i in range(satır):
    for j in range(sütun):
        if(players[i][j] == player1):
            sayac1+=1
        else:
            sayac2+=1
print("Oyuncu 1 skor : ",sayac1)
print("Oyuncu 2 skor : ",sayac2)
if(sayac1>sayac2):
    print("Oyuncu 1 kazandı ! Tebrikler...")
elif(sayac2>sayac1):
    print("Oyuncu 2 kazandı ! Tebrikler...")
else:
    print("Oyun Berabere bitti...")
