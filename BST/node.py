class Node(object):
	def __init__(self, value, left = None, right = None):
		self.left = left
		self.right = right
		self.value = value

	def isLeaf(self):
		return self.left == None and self.right == None

	def setRightChild(self, node):
		self.right = node

	def setLeftChild(self, node):
		self.left = node

	def getRightChild(self):
		return self.right

	def getLeftChild(self):
		return self.left


