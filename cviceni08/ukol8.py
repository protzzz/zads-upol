"""
#8 (5.4 - RB stromy): HOTOVO

1. Použijte RB strom pro ukládání počtu bodů u studentů.
2. Napište funkce:
    pridej_body(s,jmeno,body) – která vloží do stromu osobu se jménem jmeno a body. Pokud tato osoba ve stromu již bude, tak mu body přidá.
    body_celkem(s,jmeno) – která pro daného studenta počet získaných bodů, případně informaci, že student není v seznamu.
"""


RED = True
BLACK = False

def create_node(key, value, color=RED, left=None, right=None):
    return {"key": key, "value": value, "color": color, "left": left, "right": right}

def is_red(node):
    return node is not None and node["color"] == RED

def rotate_left(node):
    new_node = node["right"]
    node["right"] = new_node["left"]
    new_node["left"] = node
    new_node["color"] = node["color"]
    node["color"] = RED
    return new_node

def rotate_right(node):
    new_node = node["left"]
    node["left"] = new_node["right"]
    new_node["right"] = node
    new_node["color"] = node["color"]
    node["color"] = RED
    return new_node

def flip_colors(node):
    node["color"] = RED
    node["left"]["color"] = BLACK
    node["right"]["color"] = BLACK

def put(node, key, value):
    if node is None:
        return create_node(key, value, color=RED)
    
    if key < node["key"]:
        node["left"] = put(node["left"], key, value)
    elif key > node["key"]:
        node["right"] = put(node["right"], key, value)
    else:
        node["value"] += value
        return node
    
    if is_red(node["right"]) and not is_red(node["left"]):
        node = rotate_left(node)
    if is_red(node["left"]) and is_red(node["left"]["left"]):
        node = rotate_right(node)
    if is_red(node["left"]) and is_red(node["right"]):
        flip_colors(node)
    
    return node

def get(node, key):
    while node is not None:
        if key < node["key"]:
            node = node["left"]
        elif key > node["key"]:
            node = node["right"]
        else:
            return node["value"]
    return None


def pridej_body(node, jmeno, body):
    if node is None:
        return create_node(jmeno, body, BLACK)
    
    if jmeno < node["key"]:
        node["left"] = pridej_body(node["left"], jmeno, body)
    elif jmeno > node["key"]:
        node["right"] = pridej_body(node["right"], jmeno, body)
    else:
        node["value"] += body
        return node
    
    if is_red(node["right"]) and not is_red(node["left"]):
        node = rotate_left(node)
    if is_red(node["left"]) and is_red(node["left"]["left"]):
        node = rotate_right(node)
    if is_red(node["left"]) and is_red(node["right"]):
        flip_colors(node)
    
    return node

def body_celkem(node, jmeno):
    body = get(node, jmeno)
    if body is not None:
        print(f"Student {jmeno} má {body} bodů.")
    else:
        print(f"Student {jmeno} není v seznamu.")


# Použití
t = None

t = pridej_body(t,"Pavel",2)
t = pridej_body(t,"Jirka",1)
t = pridej_body(t,"Alena",3)
t = pridej_body(t,"Pavel",4)
t = pridej_body(t,"Pavel",6)
t = pridej_body(t,"Jirka",2)

body_celkem(t,"Pavel")
body_celkem(t,"Karel")