# Create separate figures for each sentence's Conceptual Dependency representation

# Create a directed graph for Sentence 1
G1 = nx.DiGraph()

# Nodes for Sentence 1
G1.add_node("GIVE", shape='box')
G1.add_node("John", shape='ellipse')
G1.add_node("Mary", shape='ellipse')
G1.add_node("Book", shape='ellipse')
G1.add_node("General", shape='ellipse')

# Edges for Sentence 1
G1.add_edges_from([("John", "GIVE"), ("Mary", "GIVE"), ("Book", "GIVE"), ("General", "Book")])

# Draw Sentence 1
plt.figure(figsize=(6, 6))
pos1 = nx.spring_layout(G1)  # positions for all nodes
nx.draw(G1, pos1, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold')
plt.title("CD Representation of Sentence 1")
plt.axis('off')
plt.show()

# Create a directed graph for Sentence 2
G2 = nx.DiGraph()

# Nodes for Sentence 2
G2.add_node("GIVE", shape='box')
G2.add_node("John", shape='ellipse')
G2.add_node("Mary", shape='ellipse')
G2.add_node("The Book", shape='ellipse')
G2.add_node("Specific", shape='ellipse')
G2.add_node("Yesterday", shape='ellipse')

# Edges for Sentence 2
G2.add_edges_from([("John", "GIVE"), ("Mary", "GIVE"), ("The Book", "GIVE"), ("Specific", "The Book"), ("Yesterday", "GIVE")])

# Draw Sentence 2
plt.figure(figsize=(6, 6))
pos2 = nx.spring_layout(G2)  # positions for all nodes
nx.draw(G2, pos2, with_labels=True, node_size=3000, node_color='lightgreen', font_size=10, font_weight='bold')
plt.title("CD Representation of Sentence 2")
plt.axis('off')
plt.show()
