def tree_insert(T, z):
    y = None
    x = T["root"]
    while x != None:
        y = x
        if z["key"] < x["key"]:
            x = x["left"]
        else:
            x = x["right"]
    z["parent"] = y
    if y == None:
        T["root"] = z
    else:
        if z["key"] < y["key"]:
            y["left"] = z
        else:
            y["right"] = z

tree_insert(0, "None")

def print_tree(x,i):
    if x != None:
        print("-"*(2*i),x["key"])
        i+=1
        print_tree(x["left"],i)
        print_tree(x["right"],i)

def tree_search(x,k):
    if x == None or k == x["key"]:
        return x
    if k < x["key"]:
        return tree_search(x["left"], k)
    else:
        return tree_search(x["right"], k)

def tree_search_iterative(x,k):
    while x != None and k != x["key"]:
        if k < x["key"]:
            x=x["left"]
        else:
            x=x["right"]
    return x

def in_order_walk(x):
    if x != None:
        in_order_walk(x["left"])
        print(x["key"],end=" ")
        in_order_walk(x["right"])

def tree_min(x):
    while x["left"] != None:
        x=x["left"]
    return x

def tree_max(x):
    while x["right"] != None:
        x=x["right"]
    return x

def tree_swap(t,u,v):
    if t["root"] == u:
        t["root"] = v
        return
    y = u["parent"]
    if u==y["left"]:
        y["left"]=v
    if u==y["right"]:
        y["right"]=v

def node_swap(t,u,v):
    v["left"]=u["left"]
    v["right"]=u["right"]
    if t["root"]==u:
        t["root"]=v
        return
    y=u["parent"]
    if u==y["left"]:
        y["left"]=v
    if u==y["right"]:
        y["right"]=v

def tree_delete(t,z):
    if z["left"] == None:
        tree_swap(t,z,z["right"])
        return
    if z["right"] == None:
        tree_swap(t,z,z["left"])
        return
    y=tree_min(z["right"])
    tree_delete(t,y)
    node_swap(t,z,y)

