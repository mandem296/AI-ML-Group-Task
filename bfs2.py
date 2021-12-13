import networkx as nx
import matplotlib.pyplot as plt
from queue import PriorityQueue


nodes=["SportsComplex","Siwaka","PH.1A","PH.1B","STC","Phase2","ParkingLot","Phase3","J1","Mada"]

t = 10
graph = [[] for i in range(t)]
def bfs(start, finish, n):
    traversed = [0] * n
    traversed = True
    pq = PriorityQueue()
    pq.put((0, start))
    while pq.empty() == False:
        u = pq.get()[1]
        # path with lowest cost
        print(u, end=" ")
        if u == finish:
            break

        for t, c in graph[u]:
            if traversed[t] == False:
                traversed[t] = True
                pq.put((c, t))
    print()
def addedge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))
addedge("SportsComplex","Siwaka","450")
addedge("Siwaka","PH.1A","10")
addedge("PH.1A","PH.1B","100")
addedge("Siwaka","PH.1B","230")
addedge("PH.1B","STC","50")
addedge("PH.1B","Phase2","112")
addedge("STC","Phase2","50")
addedge("Phase2","J1","600")
addedge("Phase2","Phase3","500")
addedge("Phase3","ParkingLot","350")
addedge("J1","Mada","200")
addedge("ParkingLot","Mada","700")
addedge("PH.1A","Mada","850")

start = "SportsComplex"
finish = "ParkingLot"

bfs(start, finish, t)
