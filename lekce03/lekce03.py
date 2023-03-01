def lenght(array):
    return len(array)

def init_stack(n):
    k = [None for x in range(n)]
    s={"data":k, "top":0}
    return s

def init_queue(n):
    k=[None for x in range(n)]
    s={"data":k, "head":0, "tail":0}
    return s

def empty(q):
    return q["head"] == q["tail"]

def full(q):
    return (q["tail"] + 1) % lenght(q["data"]) == q["head"]

def enqueue(q,x):
    if not full(q):
        q["data"][q["tail"]] = x
        q["tail"] = (q["tail"] + 1)%lenght(q["data"])

def dequeue(q):
    if not empty(q):
        x = q["data"][q["head"]]
        q["head"] = (q["head"] + 1)%lenght(q["data"]) 
        return x
    else:
        return None
    
def nth(r,n):
    nn = 1
    x = r
    while x != None and nn < n:
        x = x["next"]
        nn = nn + 1
    return x

def insert_nth(r, added, n):
    if n == 1:
        return insert_at_the_start(r,added)
    

    
    
def remove_after(r):
    ret = r["next"]
    if r["next"] != None:
        r["next"] = r["next"]["next"]
    return ret

def remove_nth(r,n):
    if n == 0:
        return r["next"], r
    x = nth(r, n-1)
    if x != None:
        x = remove_after(x)
    return r,x

def remove(r,d):
    if r == d:
        x = r
    while x["next"] != d:
        x = x["next"]
    remove_after(x)
    return r

def search(r,k):
    x = r
    while x != None and x["key"] != k:
        x = x["next"]
    return x

def concatenate(r,s):
    if r == None:
        return s
    if s == None:
        return r
    x = r
    while x["next"] != None:
        x = x["next"]
    x["next"] = s
    return r