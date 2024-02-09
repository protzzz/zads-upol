seznam_knih = []
def pridej_knihu(nazev,autor_jmeno,autor_prijmeni):
    seznam_knih.append({"nazev":nazev,"jmeno":autor_jmeno,"prijmeni":autor_prijmeni})
    return seznam_knih

pridej_knihu("Algoritmy v C","Robert","Sedgewick")
pridej_knihu("The Art of Computer Programming, Volume 1","Donald","Knuth")
pridej_knihu("The Art of Computer Programming, Volume 2","Donald","Knuth")
print(seznam_knih)

dodat_seznam = []
for i in seznam_knih:
  dodat_seznam.append({i["nazev"]:False})


def vypujceni(nazev):
   for i in seznam_knih:
      if i["nazev"] == nazev:
         for j in dodat_seznam:
            for k in j:
               if k == nazev:
                  j[k] = True
   return dodat_seznam

def vraceni(nazev):
   for i in seznam_knih:
      if i["nazev"] == nazev:
         for j in dodat_seznam:
            for k in j:
               if k == nazev:
                  j[k] = False
   return dodat_seznam

vypujceni("The Art of Computer Programming, Volume 1")
vypujceni("The Art of Computer Programming, Volume 2")

vraceni("The Art of Computer Programming, Volume 2")

vypujceni("Algoritmy v C")


print(dodat_seznam)

seznam_vyp = []
def vypujcene_knihy():
   for i in dodat_seznam:   
         for j in i:
            if i[j] == True:
             seznam_vyp.append({"nazev":j})
   return seznam_vyp

vk= vypujcene_knihy()
print("Seznam vypůjčených knih:")
for k in vk:
    print(k["nazev"])