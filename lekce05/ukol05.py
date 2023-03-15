def vloz_do_seznamu(s, jmeno):
    y = None
    x = s["root"]
    while x != None:
        y = x
        if jmeno["string"] < x["string"]:
            x = x["left"]
        else:
            x = x["right"]
    jmeno["parent"] = y
    if y == None:
        s["root"] = jmeno
    else:
        if jmeno["string"] < y["string"]:
            y["left"] = jmeno
        else:
            y["right"] = jmeno

def tisk_seznamu(s):
    if s != None:
        tisk_seznamu(s["left"])
        print(s["string"],end=" ")
        tisk_seznamu(s["right"])

def odeber_ze_seznamu(s,jmeno):

    return

# seznam=["Pavel","Jitka","Alice","Karel","David"]
# osoby={"root":None}
# for i in seznam:
#     vloz_do_seznamu(osoby,i)
# tisk_seznamu(osoby)
# odeber_ze_seznamu(osoby,"Alice")
# tisk_seznamu(osoby)