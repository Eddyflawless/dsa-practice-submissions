class Graph:
    def __init__(self, P):
        self.P = P #no of vertices
        self.adj = [ [] for i in range(P)]
        self.visited = set()


    def addEdge(self,u,v):
        if u > self.P or v > self.P:
            raise Exception(f"vertex can only be less than {self.P}")
        self.adj[u].append(v)


    def DFS(self,node):

        stack = []
        stack.append(node)

        while len(stack) != 0:
            v = stack[-1]
            stack.pop()

            #check if current node isnot visited
            if v not in self.visited:
                self.visited.add(v)

            #explote adjacent nodes
            for g in self.adj[v]:
                if g not in self.visited: #prevents cycle visits
                    stack.append(g)
                

        print(self.visited)


if __name__ == '__main__':
    g = Graph(5); # Total 5 vertices in graph
    g.addEdge(1, 0);
    g.addEdge(0, 2);
    g.addEdge(2, 1);
    g.addEdge(0, 3);
    g.addEdge(1, 4);
    
    g.DFS(0)
 