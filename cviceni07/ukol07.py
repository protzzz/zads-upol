def tree_insert(T, z):
    if T["root"] == None:
        T["root"] = z
        z["parent"] = None
        z["left"] = None
        z["right"] = None
        return

    y = None
    x = T["root"]
    while x != None:
        y = x
        if z["rok"] < x["rok"]:
            x = x["left"]
        elif z["rok"] > x["rok"]:
            x = x["right"]
        else:
            if z["ctvrtleti"] < x["ctvrtleti"]:
                x = x["left"]
            else:
                x = x["right"]
    z["parent"] = y
    z["left"] = None
    z["right"] = None
    if z["rok"] < y["rok"]:
        y["left"] = z
    elif z["rok"] > y["rok"]:
        y["right"] = z
    else:
        if z["ctvrtleti"] < y["ctvrtleti"]:
            y["left"] = z
        else:
            y["right"] = z


def insert_node(T, rok, ctvrtleti, hdp):
    z = {"rok": rok, "ctvrtleti": ctvrtleti, "hdp": hdp}
    tree_insert(T, z)


def najdi_hdp(T, rok, ctvrtleti):
    x = T["root"]
    while x != None:
        if x["rok"] == rok and x["ctvrtleti"] == ctvrtleti:
            return f"HDP v {ctvrtleti} čtvrtletí roku {rok} bylo: {x['hdp']}"
        elif x["rok"] < rok or (x["rok"] == rok and x["ctvrtleti"] < ctvrtleti):
            x = x["right"]
        else:
            x = x["left"]
    return "Tento údaj není k dispozici."


T = {"root": None}

insert_node(T, 2022, 1, 1.1)
insert_node(T, 2021, 2, -2.1)
insert_node(T, 2022, 4, 0.1)
insert_node(T, 2021, 3, 2.3)
insert_node(T, 2021, 4, -0.5)
insert_node(T, 2022, 2, -1.3)
insert_node(T, 2022, 3, 3.2)
insert_node(T, 2021, 1, 4.1)

print(najdi_hdp(T, 2021, 1))
print(najdi_hdp(T, 2022, 3))
print(najdi_hdp(T, 2023, 1))