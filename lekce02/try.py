def create_array(n):
    k = [{"key": None, "data": None}for x in range(n)]
    s = {"keys": k, "top": 0}
    return s


def insert(ar, k):
    if ar["top"] < len(ar["keys"]):
        ar["keys"][ar["top"]] = k
        ar["top"] = ar["top"] + 1


pocet = 50
array_set = create_array(pocet)

f = open("ukol-1.txt", "rt", encoding="utf-8")

for radek in f:
    s = radek.split(";")
    insert(array_set, {"key": int(s[0]), "data": s[1]})


def binary_search(ar, k):
    l = 0
    p = ar["top"] - 1
    while l <= p:
        s = (l + p) // 2

        if ar["keys"][s]["key"] == k:

            return array_set["keys"][s]["data"]

        if ar["keys"][s]["key"] < k:

            p = s - 1

        if ar["keys"][s]["key"] > k:

            l = s + 1

    if array_set["keys"][s]["data"] != k:

        return "Tento rok se nic nestalo"


print("Rok 416:" + binary_search(array_set, 416))

print("Rok 413:" + binary_search(array_set, 413))
