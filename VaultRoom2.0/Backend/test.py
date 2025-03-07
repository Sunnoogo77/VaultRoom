#import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph for the roadmap
roadmap = nx.DiGraph()

# Add nodes (certifications)
certifications = [
    "AZ-900: Microsoft Azure Fundamentals",
    "SC-900: Security, Compliance, and Identity Fundamentals",
    "MD-102: Modern Desktop Administrator",
    "SC-200: Security Operations Analyst",
    "Cisco CyberOps Associate",
    "AZ-500: Azure Security Engineer"
]

# Add dependencies (edges)
dependencies = [
    ("AZ-900: Microsoft Azure Fundamentals", "SC-900: Security, Compliance, and Identity Fundamentals"),
    ("SC-900: Security, Compliance, and Identity Fundamentals", "MD-102: Modern Desktop Administrator"),
    ("MD-102: Modern Desktop Administrator", "SC-200: Security Operations Analyst"),
    ("SC-200: Security Operations Analyst", "Cisco CyberOps Associate"),
    ("Cisco CyberOps Associate", "AZ-500: Azure Security Engineer")
]

# Add nodes and edges to the graph
roadmap.add_nodes_from(certifications)
roadmap.add_edges_from(dependencies)

# Draw the graph
plt.figure(figsize=(12, 8))
pos = nx.shell_layout(roadmap)  # Layout for better visualization
nx.draw(
    roadmap, pos, with_labels=True, node_size=3500, node_color="skyblue",
    font_size=10, font_weight="bold", edge_color="gray", arrowsize=20
)
plt.title("Certification Roadmap", fontsize=14, fontweight="bold")
plt.show()

# Save the graph as an image for download
file_path = "/mnt/data/Certification_Roadmap.png"

plt.figure(figsize=(12, 8))
pos = nx.shell_layout(roadmap)
nx.draw(
    roadmap, pos, with_labels=True, node_size=3500, node_color="skyblue",
    font_size=10, font_weight="bold", edge_color="gray", arrowsize=20
)
plt.title("Certification Roadmap", fontsize=14, fontweight="bold")
plt.savefig(file_path, format="png")
file_path