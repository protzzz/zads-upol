knihovna = []

def pridej_knihu (nazev, autor_jmeno, autor_prijmeni):
    kniha = {"nazev": nazev, "autor": f"{autor_jmeno} {autor_prijmeni}", "vypujcena": False}
    knihovna.append(kniha)

def vypujceni(nazev):
    for kniha in knihovna:
        if kniha["nazev"] == nazev:
            kniha["vypujcena"] == True
            break

def vraceni(nazev):
    for kniha in knihovna:
        if kniha["nazev"] == nazev:
            kniha["vypujcena"] == False
            break

def vypujcene_knihy():
    vypujcene_knihy = []
    for kniha in knihovna:
        if kniha["vypujcena"]:
            vypujcene_knihy.append(kniha)
    return vypujcene_knihy


vk = vypujcene_knihy()
print("Seznam vypůjčených knih:")
for k in vk:
    print(k["nazev"])

pridej_knihu("Algoritmy v C","Robert","Sedgewick")
pridej_knihu("The Art of Computer Programming, Volume 1","Donald","Knuth")
pridej_knihu("The Art of Computer Programming, Volume 2","Donald","Knuth")
vypujceni("The Art of Computer Programming, Volume 1")
vypujceni("The Art of Computer Programming, Volume 2")

    
