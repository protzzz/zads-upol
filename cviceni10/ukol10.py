def hashuj_klic(klic, velikost_tabulky):
    return hash(str(klic)) % velikost_tabulky

def hashuj_dalsi_krok(klic, velikost_tabulky):
    return 1 + (hash(str(klic)) % (velikost_tabulky - 1))

def vloz_udalost_do_tabulky(tabulka, klic, hodnota):
    index = hashuj_klic(klic, len(tabulka))
    dalsi_krok = hashuj_dalsi_krok(klic, len(tabulka))

    while tabulka[index] is not None:
        if tabulka[index][0] == klic:
            break
        index = (index + dalsi_krok) % len(tabulka)

    tabulka[index] = (klic, hodnota)

def hledej_rok(tabulka, klic):
    index = hashuj_klic(klic, len(tabulka))
    dalsi_krok = hashuj_dalsi_krok(klic, len(tabulka))

    while tabulka[index] is not None:
        if tabulka[index][0] == klic:
            return tabulka[index][1]
        index = (index + dalsi_krok) % len(tabulka)

    return "Tento rok se nic nestalo."

# použití funkce pro načtení dat ze souboru a uložení do hashovací tabulky
table = [None] * 1000
with open("ukol10.txt", "r", encoding="utf-8") as file:
    for line in file:
        parts = line.split(';')
        year = int(parts[0])
        description = " ".join(parts[1:])
        vloz_udalost_do_tabulky(table, year, description)

# testování funkce hledej_rok
print("Rok 650:" + hledej_rok(table,650))
print("Rok 100:" + hledej_rok(table,100))
