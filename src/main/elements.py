class Node:
	def __init__(self, position, mass, arguments):
		self.position = position
		self.mass = mass
		self.arguments = arguments
		
	
class Beam:
	def __init__(self, n1, n2, length, deform_threshold, break_threshold, stiffness, damping):
		self.n1 = n1
		self.n2 = n2
		self.length = length
		self.deform_threshold = deform_threshold
		self.break_threshold = break_threshold
		self.stiffness = stiffness
		self.damping = damping
		
