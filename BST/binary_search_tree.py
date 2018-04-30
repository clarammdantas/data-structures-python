from node import Node

class BST(object):

	def __init__(self, root = None):
		self.root = root

	def insert(self, node_to_insert):
		self.insert_aux(self.root, node_to_insert)

	def insert_aux(self, root, node_to_insert):
		if root is None:
			self.root = node_to_insert

		else:
			if root.value < node_to_insert.value:
				if root.get_right_child() is None:
					root.set_right_child(node_to_insert)

				else:
					self.insert_aux(root.get_right_child(), node_to_insert)

			else:
				if root.get_left_child() is None:
					root.set_left_child(node_to_insert)

				else:
					self.insert_aux(root.get_left_child(), node_to_insert)

	def search(self, value_to_search):
		value_found = self.search_aux(self.root, value_to_search)

		return value_found

	def search_aux(self, root, value_to_search):
		if root and root.value == value_to_search:
			return root.value

		if root is None:
			return "This apple isn't in this tree :("

		if root.value < value_to_search and root.get_right_child():
			return self.search_aux(root.get_right_child(), value_to_search)

		return self.search_aux(root.get_left_child(), value_to_search)

	def inorder(self):
		self.inorder_aux(self.root)

	def inorder_aux(self, root):
		if root is not None:
			self.inorder_aux(root.get_left_child())
			print root.value
			self.inorder_aux(root.get_right_child())

tree = BST()
tree.insert(Node(50))
tree.insert(Node(30))
tree.insert(Node(20))
tree.insert(Node(40))
tree.insert(Node(70))
tree.insert(Node(60))
tree.insert(Node(80))

print tree.search(50)
print tree.search(20)
print tree.search(80)
print tree.search(1)
print tree.search(70)
print tree.search(60)
print tree.search(40)
print tree.search(30)
