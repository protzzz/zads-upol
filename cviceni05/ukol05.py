def create_node(key):
    return {'key': key, 'left': None, 'right': None}

def insert_node(node, key):
    if node is None:
        return create_node(key)
    if key < node['key']:
        node['left'] = insert_node(node['left'], key)
    elif key > node['key']:
        node['right'] = insert_node(node['right'], key)
    return node

def print_tree(node):
    if node:
        print_tree(node['left'])
        print(node['key'], end=' ')
        print_tree(node['right'])

def delete_node(node, key):
    if node is None:
        return node
    if key < node['key']:
        node['left'] = delete_node(node['left'], key)
    elif key > node['key']:
        node['right'] = delete_node(node['right'], key)
    else:
        if node['left'] is None:
            temp = node['right']
            node = None
            return temp
        elif node['right'] is None:
            temp = node['left']
            node = None
            return temp
        temp = min_value_node(node['right'])
        node['key'] = temp['key']
        node['right'] = delete_node(node['right'], temp['key'])
    return node


def min_value_node(node):
    current = node
    while current['left'] is not None:
        current = current['left']
    return current

seznam = ["Pavel", "Jitka", "Alice", "Karel", "David"]
osoby = None
for i in seznam:
    osoby = insert_node(osoby, i)

print("Seznam osob:", end=' ')
print_tree(osoby)
print()

osoby = delete_node(osoby, "Alice")

print("Seznam osob: ", end=' ')
print_tree(osoby)