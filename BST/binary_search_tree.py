from node import Node

class BST(object):

	def __init__(self, root = None):
		self.root = root

	def insert(self, nodeToInsert):
		self.insert_aux(self.root, nodeToInsert)

	def insert_aux(self, root, nodeToInsert):
		if root is None:
			self.root = nodeToInsert

		else:
			if root.value < nodeToInsert.value:
				if root.getRightChild() is None:
					root.setRightChild(nodeToInsert)

				else:
					self.insert_aux(root.getRightChild(), nodeToInsert)

			else:
				if root.getLeftChild() is None:
					root.setLeftChild(nodeToInsert)

				else:
					self.insert_aux(root.getLeftChild(), nodeToInsert)

	def inorder(self):
		self.inorder_aux(self.root)

	def inorder_aux(self, root):
		if root is not None:
			self.inorder_aux(root.getLeftChild())
			print root.value
			self.inorder_aux(root.getRightChild())

tree = BST()
tree.insert(Node(50))
tree.insert(Node(30))
tree.insert(Node(20))
tree.insert(Node(40))
tree.insert(Node(70))
tree.insert(Node(60))
tree.insert(Node(80))

tree.inorder()
