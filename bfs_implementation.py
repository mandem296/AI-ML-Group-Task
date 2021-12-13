import networkx as nx
import matplotlib.pyplot as plt
from classes.bfs import BfsTraverser
G = nx.Graph()
nodes=["SportsComplex","Siwaka","PH.1A","PH.1B","STC","Phase2","ParkingLot","Phase3","J1","Mada"]
G.add_nodes_from(nodes)
G.nodes()#confirm nodes
#Add Edges and their weights
G.add_edge("SportsComplex","Siwaka",weight="450")
G.add_edge("Siwaka","PH.1A",weight="10")
G.add_edge("PH.1A","PH.1B",weight="100")
G.add_edge("Siwaka","PH.1B",weight="230")
G.add_edge("PH.1B","STC",weight="50")
G.add_edge("PH.1B","Phase2",weight="112")
G.add_edge("STC","Phase2",weight="50")
G.add_edge("Phase2","J1",weight="600")
G.add_edge("Phase2","Phase3",weight="500")
G.add_edge("Phase3","ParkingLot",weight="350")
G.add_edge("J1","Mada",weight="200")
G.add_edge("ParkingLot","Mada",weight="700")
G.add_edge("PH.1A","Mada",weight="850")


#nodes=["SportsComplex","Siwaka","PH.1A","PH.1B","STC","Phase2","ParkingLot","Phase3","J1","Mada"]


#position the nodes to resemble Madaraka's map
G.nodes["SportsComplex"]['pos']=(0,600)
G.nodes["Siwaka"]['pos']=(100,600)
G.nodes["PH.1A"]['pos']=(200,600)
G.nodes["PH.1B"]['pos']=(200,400)
G.nodes["STC"]['pos']=(200,200)
G.nodes["Phase2"]['pos']=(300,400)
G.nodes["ParkingLot"]['pos']=(400,0)
G.nodes["Phase3"]['pos']=(400,200)
G.nodes["J1"]['pos']=(400,400)
G.nodes["Mada"]['pos']=(500,400)
#store all positions in a variable
node_pos = nx.get_node_attributes(G,'pos')
#call BFS to return set of all possible routes to the goal
route_bfs = BfsTraverser()
routes = route_bfs.BFS(G,"SportsComplex","ParkingLot")
print(route_bfs.visited)
route_list = route_bfs.visited
#color the nodes in the route_bfs
node_col = ['darkturquoise' if not node in route_list else 'peru' for node in G.nodes()]
peru_colored_edges = list(zip(route_list,route_list[1:]))
#color the edges as well
#print(peru_colored_edges)
edge_col = ['darkturquoise' if not edge in peru_colored_edges else 'peru' for edge in G.edges()]
arc_weight=nx.get_edge_attributes(G,'weight')
nx.draw_networkx(G, node_pos,node_color= node_col, node_size=450)
nx.draw_networkx_edges(G, node_pos,width=2,edge_color= edge_col)
#nx.draw_networkx_edge_labels(G, node_pos,edge_color= edge_col, edge_labels=arc_weight)

nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)
plt.axis('off')
plt.show()

