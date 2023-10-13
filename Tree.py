class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

class Tree:
    def __init__(self, root):
        self.root = root

    def add_child(self, parent_node, child_node):
        parent_node.children.append(child_node) # Append para adicionar o filho ao nó da lista -> parent_node(pai) -> children(lista de filhos) 

    def display(self):
        self._display_rec(self.root, 0)  # Começa com a raiz e profundidade 0

    def _display_rec(self, node, depth):
        print('  ' * depth + str(node.data))  # Imprime o nó atual com indentações baseadas na profundidade
        for child in node.children:
            self._display_rec(child, depth+1)  # Chama recursivamente para cada filho, aumentando a profundidade

# Criando a árvore como antes
root = Node(1)
tree = Tree(root)

node2 = Node(2)
node3 = Node(3)

tree.add_child(root, node2)
tree.add_child(root, node3)

node4 = Node(4)
node5 = Node(5)

tree.add_child(node2, node4)
tree.add_child(node2, node5)

# Imprimindo a árvore
tree.display()
