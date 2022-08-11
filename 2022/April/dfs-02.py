
class Graph:

    def __init__(self, N):
        self.N = N #no of vertixes
        self.adj = [ [] for i in range(N)]
        self.visited = set()

    # adds an edge to graph
    def addEdge(self, u, v):
        self.adj[u].append(v)

    def dfs(self, node):

        stack = []
        stack.append(node)

        while len(stack) != 0:
            s = stack[-1]
            stack.pop()

            if s not in self.visited:
                self.visited.add(s)

            for node in self.adj[s]:
                if node not in self.visited:
                    stack.append(node)



if __name__ == '__main__':

    g = Graph(5); # Total 5 vertices in graph
    g.addEdge(1, 0);
    g.addEdge(0, 2);
    g.addEdge(2, 1);
    g.addEdge(0, 3);
    g.addEdge(1, 4);
    
    print("Following is Depth First Traversal")
    g.DFS(0)



   
