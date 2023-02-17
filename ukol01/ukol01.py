kniha = []
stav = False

def pridej_knihu(nazev, autor_jmeno, autor_prijmeni):
    kniha = {"nazev":nazev, "autor_jmeno":autor_jmeno, "autor_prijmeni":autor_prijmeni}
    print(kniha)

def vypujceni(nazev):
    for i in kniha:
        if i["nazev"] == nazev:
            stav = True

def vraceni(nazev):
    for i in kniha:
        if i["nazev"] == nazev:
            stav = False

def vypujceni_knihy():
    for i in kniha:
        if stav == True:
            print(kniha[i])

pridej_knihu("Algoritmy v C","Robert","Sedgewick")
pridej_knihu("TheArt ofComputerProgramming, Volume1","Donald","Knuth")
pridej_knihu("TheArt ofComputerProgramming, Volume2","Donald","Knuth")

vypujceni("TheArt ofComputerProgramming, Volume1")
vypujceni("TheArt ofComputerProgramming, Volume2")


print("Seznam vypůjčených knih:")
vypujceni_knihy()