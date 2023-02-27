def create_array(n):
    k = [{"key": None, "data": None} for x in range(n)]
    s = {"keys": k, "top": 0}
    return s

def insert(arr, record):
    if arr["top"] < len(arr["keys"]):
        arr["keys"][arr["top"]] = record
        arr["top"] = arr["top"] + 1

def binary_search(arr, year):
    left = 0
    right = arr["top"] - 1
    while left <= right:
        mid = (left + right) // 2
        if arr["keys"][mid]["key"] == year:
            return arr["keys"][mid]["data"]
        elif arr["keys"][mid]["key"] < year:
            left = mid + 1
        else:
            right = mid - 1
    return "Tento rok se neexestuje."

pocet = 50
array_set = create_array(pocet)
f = open("ukol-1.txt", "rt", encoding = "utf-8")

for radek in f:
    s = radek.split(";")
    insert(array_set, {"key": int(s[0]), "data": s[1].strip()})

print("Rok 371: " + binary_search(array_set, 371))
print("Rok 100: " + binary_search(array_set, 100))