#hash maps holds the address to the nodes 
class Node:
    
    prev = None
    next = None
    
    def __init__(self, key, value):
        self.key = key
        self.value = value


class LRUCache:
    
    lruPtr = Node(0,0) #least recently used
    mruPtr = Node(0,0) #most recently used
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        
        self.lruPtr.next = self.mruPtr
        self.mruPtr.prev = self.lruPtr
        
    #remove node from list    
    def remove(self, node):
        
        if node is None:
            return
        
        prev, next = node.next, node.prev
        
        if prev:
            prev.next = node.next
        
        if next:
            next.prev = node.prev    

        
    def insert(self, node):
        
        if node is None:
            return
        
        prev = self.mruPtr.prev         
        node.next = self.mruPtr
        node.prev = prev
        prev.next = node
        self.mruPtr.prev = node
     
    def get(self, key):
        
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
    
    def put(self, key, value):
        
        if key in self.cache:
            self.remove(self.cache[key])
            
        self.cache[key] = Node(key, value) #key points to memory location
        self.insert(self.cache[key]) 
        
        if len(self.cache) > self.cap:
            lru = self.lruPtr.next
            self.remove(lru)
            print("delete key: ", lru.key)
            del self.cache[lru.key]
                    
            
def runQueryOperation(arg, lruCache):
    ops = arg[0]
    if ops == 2:
        if len(arg) != 2: #ignores operations, list, not having the required number of arguments
            return
        lruCache.get(arg[1])
    elif ops == 1:
        if len(arg) != 3:
            return
        lruCache.put(arg[1], arg[2])    
        
         
def getInputArguments( queries):
    
    cacheSize = 0
    index = 0
    count = 0
    while True:
        
        arg = input()        
        arg =  cleanInput(arg)
        
        if index == 0:
            count = int(arg[0])
            cacheSize = int(arg[1])
            index += 1
            continue
        
        if index >= count:
            break
        
        queries.append(arg) 
        index += 1   
        
    return cacheSize

def cleanInput(arg):
    
    arg = str(arg)
    arg = [ s for s in arg if s != ' ' ]
    
    return arg    

if __name__ == '__main__':
    
    # queries = []
    
    # try:
    #     cacheSize = getInputArguments(queries)
        
    # except Exception as e:
    #     raise e
    
    queries = [[1,1,1], [1,2,2], [2,1], [1, 4, 3], [2,2] ]
    cacheSize = 3
                            
    print("queries: ",queries)
    print("cacheSize: ",cacheSize)
    
    lruCache = LRUCache(cacheSize)
    
    for query in queries:
        runQueryOperation(query, lruCache)
        
    # get operations    
    print("get key: of 2", lruCache.get(2) )
    print("get key of 4", lruCache.get(4) )    
    
    # put operations
    print("put key: of 3", lruCache.put(3, 15) )
    print("put key of 7", lruCache.put(7,21) )    
    print("put key of 31", lruCache.put(31,1201) ) 
    
    # get operations
    print("get key: of 3", lruCache.get(3) )
    print("get key of 7", lruCache.get(7) )    
    print("get key of 31", lruCache.get(31) ) 
    
    print("-->", len(lruCache.cache))
    