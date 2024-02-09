RED=0
BLACK=1

NIL={"c":BLACK,"key":None}

def set_left_child(p,c):
    p["left"]=c
    if c["key"] != None:
        c["parent"]=p

def set_right_child(p,c):
    p["right"]=c
    if c["key"] != None:
        c["parent"]=p

def set_root(t, x):
    t["root"] = x
    if x != None:
        x["parent"] = None

def transplant_tree(t, u, v):
    if u["parent"] == None:
        set_root(t, v)
    else:
        x = u["parent"]
        if u == x["left"]:
            set_left_child(x, v)
        else:
            set_right_child(x, v)

def rotate_left(t, x):
    y = x["right"]
    set_right_child(x, y["left"])
    transplant_tree(t, x, y)
    set_left_child(y, x)

def rotate_right(t, x):
    y = x["left"]
    set_left_child(x, y["right"])
    transplant_tree(t, x, y)
    set_right_child(y, x)

def tree_insert(T, z):
    y = None
    x = T["root"]
    while x["key"] != None:
        y = x 
        if z["key"] < x["key"]: 
            x = x["left"]
        else:
            x=x["right"]
    z["parent"]=y
    if y == None:
        T["root"]=z
    else:
        if z["key"] < y["key"]:
            y["left"]=z
        else:
            y["right"]=z

def tree_search(x,k):
    if x["key"] == None or k == x["key"]:
        return x
    if k < x["key"]:
        return tree_search(x["left"], k)
    else:
        return tree_search(x["right"], k)


def uncle(z):
    if z["parent"]["parent"]["left"]["key"]==z["parent"]["key"]:
        return z["parent"]["parent"]["right"]
    else:
        return z["parent"]["parent"]["left"]
    
def local_fix(t,z):
    u=uncle(z)
    if u["c"]==RED:
            z["parent"]["c"]=BLACK
            z["parent"]["parent"]["c"]=RED
            u["c"]=BLACK
            return z["parent"]["parent"]
    else:
        if(z["parent"]["parent"]["left"]==z["parent"]):
            if z["parent"]["right"]["key"]==z["key"]:
                rotate_left(t,z["parent"])
            z["parent"]["c"]=BLACK
            z["parent"]["parent"]["c"]=RED
            rotate_right(t,z["parent"]["parent"])
        else:
            if z["parent"]["left"]==z:
                rotate_right(t,z["parent"])
            z["parent"]["c"]=BLACK
            z["parent"]["parent"]["c"]=RED
            
            rotate_left(t,z["parent"]["parent"])
        return z["parent"]
            
def rb_fixup(t,z):
    while (z != t["root"]):
        if z["parent"]["c"] == BLACK:
            break #algoritmus končí
        z = local_fix(t,z) # procedura pro opravy, viz dalsi slajdy
    t["root"]["c"] = BLACK

def rb_insert(t,added):
    added["left"]={"c":BLACK,"key":None,"parent":added}
    added["right"]={"c":BLACK,"key":None,"parent":added}
    added["c"] = RED
    tree_insert(t, added)
    rb_fixup(t, added)

def print_tree(x,i):
    if x["key"] != None:
        print("-"*(2*i),x["key"],"(",x["c"],")")
        i+=1
        print_tree(x["left"],i)
        print_tree(x["right"],i)

tree={"root":{"c":BLACK,"key":None,"parent":None}}
u={"parent":None, "key":1}
rb_insert(tree,u)
print_tree(tree["root"],0)
print()
u={"parent":None, "key":2}
rb_insert(tree,u)
print_tree(tree["root"],0)
print()
u={"parent":None, "key":3}
rb_insert(tree,u)
print_tree(tree["root"],0)
print()
u={"parent":None, "key":4}
rb_insert(tree,u)
print_tree(tree["root"],0)
print()
u={"parent":None, "key":5}
rb_insert(tree,u)
print_tree(tree["root"],0)
print()
u={"parent":None, "key":6}
rb_insert(tree,u)
print_tree(tree["root"],0)
print()
u={"parent":None, "key":7}
rb_insert(tree,u)
print_tree(tree["root"],0)
print()
u={"parent":None, "key":8}
rb_insert(tree,u)
print_tree(tree["root"],0)
print()
u={"parent":None, "key":9}
rb_insert(tree,u)
print_tree(tree["root"],0)
print()
u={"parent":None, "key":10}

#Odebírání uzlu
def tree_min(x):
    while x["left"]["key"] != None:
        x=x["left"]
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
    v["parent"]=y

def node_swap(t,u,v):
    v["left"]=u["left"]
    v["right"]=u["right"]
    v["c"]=u["c"]
    if t["root"]==u:
        t["root"]=v
        return
    y=u["parent"]
    if u==y["left"]:
        y["left"]=v
    if u==y["right"]:
        y["right"]=v

def tree_delete(t,z):
    if z["left"]["key"] == None:
        u=z["right"]
        col=z["c"]
        tree_swap(t,z,z["right"])
        return u,col
    if z["right"]["key"] == None:
        u=z["left"]
        col=z["c"]
        tree_swap(t,z,z["left"])
        return u,col
    y=tree_min(z["right"])
    col=u["c"]
    tree_delete(t,y)
    node_swap(t,z,y)
    return y,col

def sibling(z):
    if z["parent"]["left"]==z:
        return z["parent"]["right"]
    else:
        return z["parent"]["left"]

def get_color(z):
    return z["c"]

def local_delete_fix(t,z):
    s=sibling(z)
    if get_color(s)==RED:
        s["parent"]["c"]=RED
        s["c"]=BLACK
        if z["parent"]["left"]==z:
            rotate_left(t,z["parent"])
        else:
            rotate_right(t,z["parent"])

    s=sibling(z)    
    if get_color(s["left"])==BLACK and get_color(s["right"])==BLACK:
        s["c"]=RED
        return s["parent"],False
    else:
        if get_color(s["left"])==RED and get_color(s["right"])==BLACK:
            s["c"]=RED
            s["left"]["c"]=BLACK
            rotate_right(t,s)
        s=sibling(z)
        s["right"]["c"]=BLACK
        s["parent"]["c"]=BLACK
        rotate_left(t,z["parent"])
        return z,True


    

def rb_delete_fixup(t,z):
    quit=False
    while z!=t["root"] and quit!=True:
        if get_color(z)==RED:
            z["c"]=BLACK
            break
        z,quit=local_delete_fix(t,z)

def rb_delete(t,z):
    u,col=tree_delete(t,z)
    if col!=RED:
        rb_delete_fixup(t,u)

u=tree_search(tree["root"],1)
rb_delete(tree,u)
print_tree(tree["root"],0)
print()

u=tree_search(tree["root"],2)
rb_delete(tree,u)
print_tree(tree["root"],0)
print()

u=tree_search(tree["root"],3)
rb_delete(tree,u)
print_tree(tree["root"],0)
print()