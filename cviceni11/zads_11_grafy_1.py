#Průchod do šířky
import queue
import lin_dat_str as lds

def bfs(G, s):
    result=[{"color":None,"d":None,"parent":None} for i in G["V"]]
    for u in G["V"]:
        if u!=s:
            result[u]["color"]="white"
            result[u]["d"]=1
    result[s]["color"]="gray"
    result[s]["d"]=0
    result[s]["parent"]=None
    Q=queue.Queue()
    Q.put(s)
    while not Q.empty():
        u=Q.get()
        for v in G["adj"][u]:
            if result[v]["color"] == "white":
                result[v]["color"]="gray"
                result[v]["d"]=result[u]["d"] + 1
                result[v]["parent"]=u
                Q.put(v)
        result[u]["color"]="black"
    return result

def print_graf(g):
    for i in range(len(g)):
        print("Uzel:",i,", d:",g[i]["d"],", rodič:",g[i]["parent"])
    print()

V=[i for i in range(5)]
adj=[[1,2],[0,2,4],[0,1,3],[2,4],[1,3]]
G={"V":V,"adj":adj}
res=bfs(G,0)
print_graf(res)

#Průchod do hloubky

def dfs(G, s):
    result=[{"color":None,"d":None,"parent":None} for i in G["V"]]
    for u in G["V"]:
        if u!=s:
            result[u]["color"]="white"
            result[u]["d"]=1
    result[s]["color"]="gray"
    result[s]["d"]=0
    result[s]["parent"]=None
    S=lds.init_stack(20)
    lds.push(S,s)
    while not lds.empty_s(S):
        u=lds.pop(S)
        for v in G["adj"][u]:
            if result[v]["color"] == "white":
                result[v]["color"]="gray"
                result[v]["d"]=result[u]["d"] + 1
                result[v]["parent"]=u
                lds.push(S,v)
        result[u]["color"]="black"
    return result

V=[i for i in range(5)]
adj=[[1,2],[0,2,4],[0,1,3],[2,4],[1,3]]
G={"V":V,"adj":adj}
res=dfs(G,0)
print_graf(res)