import networkx as nx

number_list = {
  'Zafran30': ['SSID 1 : Aldo']
}

G = nx.Graph(number_list)

rooms_to_connect = zip(list(number_list.keys())[:-1], list(number_list.keys())[1:])

G.add_edges_from(rooms_to_connect)
nx.draw(G, with_labels=True)