class queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
        
        
        
q=Queue()
q.isEmpty()

q.enqueue('python')
q.enqueue(5)
q=Queue()
q.isEmpty()

q.enqueue(87)
q.enqueue('git')
q.enqueue(True)



#hotpotato game importing above class 'queue'

import queue

def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

print(hotPotato(["a","b","c","x","y","z"],7))


#it returns 'c' as output




