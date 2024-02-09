def vloz_do_zebricku(s, jmeno, body):
    if s is None:
        return {"jmeno": jmeno, "body": body, "left": None, "right": None, "count": 1}
    elif body < s["body"]:
        s["left"] = vloz_do_zebricku(s["left"], jmeno, body)
        s["count"] = 1 + (s["left"]["count"] if s["left"] else 0) + (s["right"]["count"] if s["right"] else 0)
    else:
        s["right"] = vloz_do_zebricku(s["right"], jmeno, body)
        s["count"] = 1 + (s["left"]["count"] if s["left"] else 0) + (s["right"]["count"] if s["right"] else 0)
    return s

def najdi_poradi(s, k):
    if s is None:
        return None
    left_count = 0
    if s["left"] is not None:
        left_count = s["left"]["count"]
    if k == left_count + 1:
        return s["jmeno"]
    elif k <= left_count:
        return najdi_poradi(s["left"], k)
    else:
        return najdi_poradi(s["right"], k - left_count - 1)


zebricek = {"root": None}

zebricek["root"] = vloz_do_zebricku(zebricek["root"], "Garcia Caroline", 4415)
zebricek["root"] = vloz_do_zebricku(zebricek["root"], "Swiatek Iga", 11025)
zebricek["root"] = vloz_do_zebricku(zebricek["root"], "Kasatkina Darya", 3380)
zebricek["root"] = vloz_do_zebricku(zebricek["root"], "Pegula Jessica", 5000)
zebricek["root"] = vloz_do_zebricku(zebricek["root"], "Sabalenka Aryna", 4340)
zebricek["root"] = vloz_do_zebricku(zebricek["root"], "Gauff Cori", 3871)
zebricek["root"] = vloz_do_zebricku(zebricek["root"], "Kudermetova Veronika", 2715)
zebricek["root"] = vloz_do_zebricku(zebricek["root"], "Keys Madison", 2597)
zebricek["root"] = vloz_do_zebricku(zebricek["root"], "Sakkari Maria", 3921)
zebricek["root"] = vloz_do_zebricku(zebricek["root"], "Jabeur Ons", 5180)
zebricek["root"] = vloz_do_zebricku(zebricek["root"], "Kasatkina Darya", 3380)

print("1. hráčkou žebříčku WTA je ", najdi_poradi(zebricek["root"], 1))
print("8. hráčkou žebříčku WTA je ", najdi_poradi(zebricek["root"], 8))
