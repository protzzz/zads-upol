import lin_dat_str as lds

root={"id":1,"children":[
    {"id":2,"children":[
        {"id":5,"children":[],"n":0},
        {"id":6,"children":[
            {"id":10,"children":[],"n":0},
            {"id":11,"children":[],"n":0},
            {"id":12,"children":[],"n":0}],"n":3},
        {"id":7,"children":[],"n":0}],"n":3},
    {"id":3,"children":[],"n":0},
    {"id":4,"children":[
        {"id":8,"children":[],"n":0},
        {"id":9,"children":[],"n":0}],"n":2}],"n":3}

def depth_first_search(node):
    x=node
    print(x["id"], end=" ")
    for i in range(x["n"]):
        depth_first_search(x["children"][i])

def breadth_first_search_iter(node):
    x=node
    Q=lds.init_queue(20)
    lds.enqueue(Q,x)
    while lds.empty_q(Q)!=True:
        y=lds.dequeue(Q)
        print(y["id"],end=" ")
        for i in range(y["n"]):
            lds.enqueue(Q,y["children"][i])

def depth_first_search_iter(node):
    x=node
    S=lds.init_stack(20)
    lds.push(S,x)
    while lds.empty_s(S)!=True:
        y=lds.pop(S)
        print(y["id"],end=" ")
        for i in range(y["n"]):
            lds.push(S,y["children"][i])

depth_first_search(root)
print()
depth_first_search_iter(root)
