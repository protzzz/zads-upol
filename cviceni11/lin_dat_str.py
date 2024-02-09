#Zásobník
def length(array):
    return len(array)

def init_stack(n):
    k=[None for x in range(n)]
    s={"data":k,"top":0}
    return s


def push(S, x):
    if S["top"] < length(S["data"]):
        S["data"][S["top"]]=x
        S["top"]=S["top"] + 1

def pop(S):
    if S["top"] > 0:
        S["top"]=S["top"] - 1
        return S["data"][S["top"]]
    return None

def empty_s(S):
    return S["top"] == 0

def full_s(S):
    return S["top"] == length(S["data"])

#Fronta
def init_queue(n):
    k=[None for x in range(n)]
    s={"data":k,"head":0,"tail":0}
    return s

def empty_q(Q):
    return Q["head"] == Q["tail"]

def full_q(Q):
    return (Q["tail"] + 1)%length(Q["data"]) == Q["head"]

def enqueue(Q,x):
    if not full_q(Q):
        Q["data"][Q["tail"]]=x
        Q["tail"]=(Q["tail"] + 1)%length(Q["data"])

def dequeue(Q):
    if not empty_q(Q):
        x=Q["data"][Q["head"]]
        Q["head"]=(Q["head"] + 1)%length(Q["data"])
        return x
    else:
        return None