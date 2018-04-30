class Node(object):
	def __init__(self, value, left = None, right = None):
		self.left = left
		self.right = right
		self.value = value

	def is_leaf(self):
		return self.left == None and self.right == None

	def set_right_child(self, node):
		self.right = node

	def set_left_child(self, node):
		self.left = node

	def get_right_child(self):
		return self.right

	def get_left_child(self):
		return self.left


