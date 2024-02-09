seznam1 = []
seznam2 = []

def enqueue(x):
    seznam1.append(x)

def dequeue():
    if len(seznam1) == 0 and len(seznam2) == 0:
        return None
    elif len(seznam2) == 0:
        while len(seznam1) > 0:
            seznam2.append(seznam1.pop())
    return seznam2.pop()

for i in range(10):
    enqueue(i)

for i in range(10):
    print(dequeue(), end=",")