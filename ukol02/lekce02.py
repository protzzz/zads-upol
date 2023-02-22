def create_array(n):
    k=[{"key":None, "data":None} for x in range(n)]
    s={"keys":k, "top":0}
    return s

def insert(arr,k):
    if arr["top"] < len(arr["keys"]):
        arr["keys"] [arr["top"]] = k
        arr["top"] = arr["top"] + 1

def delete(arr,i):
    if i < arr["top"]:
        arr["keys"][i] = arr["keys"][arr["top"] - 1]
        arr["top"] = arr["top"] - 1

def print_array(arr):
    for i in range(arr["top"]):
        print(arr["keys"][i]["key"], "-", arr["keys"][i]["data"], end=", ")
    print()

def search(arr,k):
    for i in range(arr["top"]):
        if arr["keys"][i]["key"] == k:
            return i
    return -1

def key_sort(i):
    return i["key"]

def search_sort(arr,k):
    for i in range(len(arr["keys"])):
        if arr["keys"][i]["key"] == k:
            return i
        if arr["keys"][i]["key"] > k:
            return -1

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

f = create_array(20)
insert(f,{"key":1, "data":"Jirka"})
insert(f,{"key":15, "data":"Alice"})
insert(f,{"key":12, "data":"Petr"})
insert(f,{"key":21, "data":"Klara"})

print_array(f)
delete(f,2)
print_array(f)

print(search(f,15))
print(search(f,3))

l = f["keys"][:f["top"]]
l.sort(key=key_sort)
f["keys"][:f["top"]] = l

print(search_sort(f,15))
print(search_sort(f,3))
