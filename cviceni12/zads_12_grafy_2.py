#Průchod do hloubky
time=0
def dfs_all(G):
    result=[{"X":False,"D":0,"F":0,"P":None} for i in G["V"]]
    for u in G["V"]:
        if result[u]["X"] == False:
            dfs_visit(G,u,result)
    return result

def dfs_visit(G, u,result):
    global time
    time=time + 1
    result[u]["D"]=time
    result[u]["X"]=True
    for v in G["adj"][u]:
        if result[v]["X"] == False:
            result[v]["P"]=u
            dfs_visit(G,v,result)
    time=time + 1
    result[u]["F"]=time

def print_graf(g):
    for i in range(len(g)):
        print("Uzel:",i,", rodič:",g[i]["P"])
    print()

V=[i for i in range(5)]
adj=[[2],[4],[0,3],[2],[1]]
G={"V":V,"adj":adj}
res=dfs_all(G)
print_graf(res)

#Topologické uspořádání
time=0
def topol(G):
    result=[{"X":False,"D":0,"F":0,"P":None} for i in G["V"]]
    top=[]
    for u in G["V"]:
        if result[u]["X"] == False:
            dfs_visit(G,u,result,top)
    return top

def dfs_visit(G, u,result,t):
    global time
    time=time + 1
    result[u]["D"]=time
    result[u]["X"]=True
    for v in G["adj"][u]:
        if result[v]["X"] == False:
            result[v]["P"]=u
            dfs_visit(G,v,result,t)
    time=time + 1
    result[u]["F"]=time
    t.insert(0,u)

def print_top(g):
    for i in g:
        print("Uzel:",i)
    print()

V=[i for i in range(6)]
adj=[[1,2],[3],[1,3,4],[5],[3,5],[]]
G={"V":V,"adj":adj}
res=topol(G)
print_top(res)

#Dijskrtův algoritmus
def make_priority_queue():
    return []

def insert(Q,n):
    Q.append(n)

def empty(Q):
    if len(Q)==0:
        return True
    else:
        return False

def f(n):
    return n["key"]

def extract_min(Q):
    Q.sort(key=f)
    x=Q[0]
    Q.pop(0)
    return x

def decrease_key(Q, n, x):
    Q.remove(n)
    n["key"]=x
    Q.append(n)

def compute_omega(G):
    omega=1
    for u  in range(len(G["V"])):
        for node in G["adj"][u]:
            omega=omega + node["delta"]
    return omega

def dijkstra(G,s):
    omega=compute_omega(G)
    nodes=[{"key":omega,"data":i,"color":"white","parent":None} for i in range(len(G["V"]))]
    nodes[s]["key"]=0
    nodes[s]["color"]="gray"
    Q=make_priority_queue()
    insert(Q, nodes[s])
    while not empty(Q):
        m=extract_min(Q)["data"]
        for v in G["adj"][m]:
            id=v["vertex"]
            if nodes[id]["color"] != "black":
                x=nodes[m]["key"] + v["delta"]
                if x < nodes[id]["key"]:
                    nodes[id]["parent"]=m
                    if nodes[id]["color"] == "gray":
                        decrease_key(Q, nodes[id], x)
                    else:
                        nodes[id]["key"]=x
                        nodes[id]["color"]="gray"
                        insert(Q, nodes[id])
        nodes[m]["color"]="black" 
    return nodes

def print_dif(g,s):
    print("Vzdálenost od uzlu",s)
    for i in g:
        if i["data"]!=s:
            print("\tuzel:",i["data"],", vzdálenost:",i["key"])
    print()

V=[i for i in range(6)]
adj=[[{"delta":3,"vertex":1},{"delta":1,"vertex":2}],
[{"delta":3,"vertex":0},{"delta":1,"vertex":2},{"delta":4,"vertex":3},{"delta":2,"vertex":4}],
[{"delta":1,"vertex":0},{"delta":1,"vertex":1},{"delta":3,"vertex":4}],
[{"delta":4,"vertex":1},{"delta":4,"vertex":4},{"delta":5,"vertex":5}],
[{"delta":2,"vertex":1},{"delta":3,"vertex":2},{"delta":4,"vertex":4},{"delta":1,"vertex":5}],
[{"delta":5,"vertex":3},{"delta":1,"vertex":4}]]

G={"V":V,"adj":adj}
res=dijkstra(G,0)
print_dif(res,0)