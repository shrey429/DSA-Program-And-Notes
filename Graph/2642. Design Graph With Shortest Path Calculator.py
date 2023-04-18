# Simple Dijkstra only but have to modify little because :
# If we create distance array by taking n= len(self.graph) then index may get out of bound if 'node1 or node2' will be >= n.
# Also for fidning shortest path between two nodes, we don't need distance array, we can do like this only.
# we need distance array when we want to find path from source to all other nodes like that.

# So instaed of craeting any distance array, just keep on pushing the cost simply if not visited.
# first time node will be poped that will be the minimum cost only.


class Graph:
    
    def __init__(self, n: int, edges: List[List[int]]):
        self.graph= collections.defaultdict(list)
        # there may be same edge already before.
        for s,d,c in edges:
            self.graph[s].append((d, c))  

    def addEdge(self, edge: List[int]) -> None:
        s,d,c= edge
        self.graph[s].append((d, c)) 

    def shortestPath(self, node1: int, node2: int) -> int:
        n= len(self.graph)
        visited= set()
        minHeap= [(0, node1)]
        while minHeap:
            w1, n1= heapq.heappop(minHeap)
            if n1== node2:
                return w1
            if n1 in visited :
                continue
            visited.add(n1)
            for n2, w2 in self.graph[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return -1


# with distance array we can do like this.
# make distance arary with max no of nodes. but no need of distance array.
class Graph:
    
    def __init__(self, n: int, edges: List[List[int]]):
        self.maxNodes= n
        self.graph= collections.defaultdict(list)
        # there may be same edge already before.
        for s,d,c in edges:
            self.graph[s].append((d, c))  

    def addEdge(self, edge: List[int]) -> None:
        s,d,c= edge
        self.graph[s].append((d, c)) 

    def shortestPath(self, node1: int, node2: int) -> int:
        n= self.maxNodes
        distance= [float('inf')] * n
        distance[node1]= 0
        visited= set()
        minHeap= [(0, node1)]
        while minHeap:
            w1, n1= heapq.heappop(minHeap)
            if n1== node2:
                return w1
            if n1 in visited:
                continue
            visited.add(n1)
            for n2, w2 in self.graph[n1]:
                if n2 not in visited and distance[n2] > w1 + w2:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return -1