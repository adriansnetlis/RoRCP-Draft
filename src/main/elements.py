class Node:
	def __init__(self, position, mass, arguments):
		self.position = position
		self.mass = mass
		self.arguments = arguments
		self.force = [0.0, -9.8 * self.mass, 0.0] # Using lists for draft as vectors
		self.velocity = [0.0, 0.0, 0.0]
		
	def apply_force(self, force):
		self.force[0] += force[0]
		self.force[1] += force[1]
		self.force[2] += force[2]
		
	def get_delta_speed(self):
		return [self.force[0] / self.mass, self.force[1] / self.mass, self.force[2] / self.mass]
		
	def clean(self):
		self.force = [0.0, -9.8 * self.mass, 0.0]
	
class Beam:
	def __init__(self, n1, n2, length, deform_threshold, break_threshold, stiffness, damping):
		self.n1 = n1
		self.n2 = n2
		self.length = length
		self.deform_threshold = deform_threshold
		self.break_threshold = break_threshold
		self.stiffness = stiffness
		self.damping = damping
		self.prevrate = 0.0
		
	def update(self, nodelist, dt):
		no1 = nodelist[self.n1] # In C++ will propably just store pointers in self.n1 and self.n2 place which will make no need for taking in nodelist;)
		no2 = nodelist[self.n2]
		distance = ((no1.position[0] - no2.position[0]) ** 2 + (no1.position[1] - no2.position[1]) ** 2 + (no1.position[2] - no2.position[2]) ** 2) ** 0.5
		rate = distance - self.length
		force = self.stiffness * rate
		damp = (rate - self.prevrate) / dt * self.damping
		net = force + damp
		return net
