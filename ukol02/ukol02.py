def create_array(n):
    k=[{"key":None, "data":None} for x in range(n)]
    s={"keys":k, "top":0}
    return s

def insert(arr,k):
    if arr["top"] < len(arr["keys"]):
        arr["keys"] [arr["top"]] = k
        arr["top"] = arr["top"] + 1

def binarni_search(arr,k):
    l = 0
    p = arr["top"] - 1
    while l <= p:
        s = (l + p) // 2
        if arr["keys"][s]["key"] == k:
            return s
        if arr["keys"][s]["key"] > k:
            l = s - 1
        if arr["keys"][s]["key"] < k:
            l = s + 1
    return -1

pocet = 50
array = create_array(pocet)
f = open("ukol-1.txt", "rt", encoding="utf8")

for radek in f:
    s = radek.split(";")
    num = []
    insert(array, {"key":int(s[0]), "data":s[1]})


print("Rok371:"+ binarni_search(array,371))
print("Rok100:"+ binarni_search(array,100))
