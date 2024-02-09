T = 2

def create_node(leaf=False):
    node = {}
    node['leaf'] = leaf
    node['keys'] = []
    node['values'] = []
    node['children'] = []
    return node

def search(node, key):
    i = 0
    while i < len(node['keys']) and key > node['keys'][i]:
        i += 1
    if i < len(node['keys']) and key == node['keys'][i]:
        return node['values'][i]
    elif node['leaf']:
        return None
    else:
        return search(node['children'][i], key)

def insert(node, key, value):
    i = 0
    while i < len(node['keys']) and key > node['keys'][i]:
        i += 1
    if node['leaf']:
        node['keys'].insert(i, key)
        node['values'].insert(i, value)
    else:
        if len(node['children'][i]) == 2*T - 1:
            split_node = create_node(leaf=False)
            split_node['children'].append(node['children'][i])
            split_node['keys'].append(node['keys'][i])
            split_node['values'].append(node['values'][i])
            node['children'][i] = split_node
            node['keys'].insert(i, key)
            node['values'].insert(i, value)
            node['children'].insert(i+1, create_node(leaf=True))
            split_node_index = i
            if key > node['keys'][i]:
                split_node_index += 1
        else:
            split_node_index = i
        insert(node['children'][split_node_index], key, value)

def najdi_teplotu(root, den):
    value = search(root, den)
    if value is not None:
        return f"Maximální teplota {den} byla {value}°C."
    else:
        return f"Maximální teplota {den} nebyla nalezena."



root = create_node(leaf=True)

data = [{"den":"1.1.","teplota":1.1},
    {"den":"12.12.","teplota":2.3},
    {"den":"8.7.","teplota":20.1},
    {"den":"14.3.","teplota":4.3},
    {"den":"17.11.","teplota":8.1},
    {"den":"12.4.","teplota":6.2},
    {"den":"17.11.","teplota":3.8},
    {"den":"19.12.","teplota":1.8},
    {"den":"1.9.","teplota":12.3},
    {"den":"13.8.","teplota":19.6},
    {"den":"14.2.","teplota":2.2},
    {"den":"16.5.","teplota":10.7},
    {"den":"14.5.","teplota":10.5},
    {"den":"5.10.","teplota":6.2},
    {"den":"18.12.","teplota":0.4},
    {"den":"12.6.","teplota":13.1},]

for item in data:
    insert(root, item['den'], item['teplota'])

print(najdi_teplotu(root, "5.10."))
print(najdi_teplotu(root, "31.12."))
