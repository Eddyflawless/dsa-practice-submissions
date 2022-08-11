
def dfs(graph, node, visited ):

    if node not in visited:
        #print("current node: ",node)
        visited.add(node)    
        #print("visited nodes: ", visited)

        for neighbour in graph[node]:
            #print("neighbour", neighbour)
            dfs(graph, neighbour, visited)

    else:
        print(f"skip {node}")        



if __name__ == '__main__':

    graph = {
        '5' : set(['3','7']),
        '3' : set(['2', '4', '3']),
        '7' : set(['8']),
        '2' : set(['1']),
        '4' : set(['8','2']),
        '8' : set([]),
        '1' : set(['2']) 
    }

    visited = set()

    dfs(graph,'5', visited)

    print("nodes visited", visited)


   
