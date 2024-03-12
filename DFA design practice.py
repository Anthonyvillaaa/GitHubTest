class DFA:
	def __init__ (self, Q, Sigma, delta, q0, F):
		self.Q = Q	# Set of states
		self.Sigma = Sigma	# Alphabet
		self.delta = delta	# Transition function as a dictionary
		self.q0 = q0	# Start state
		self.F = F	# Set of accept states

	def __repr__(self):
		return f"DFA ({self.Q}, \n\t{self.Sigma}, \n\t{self.delta}, \n\t{self.q0}, \n\t{self.F})"
	
	def run (self,w) :
		q = self.q0
		while w!="":
			q = self.delta[(q,w[0])]
			w = w[1:]
		return q in self.F

D0 = DFA({0,1,2,3},{"a","b"},
	  {(0, "b"):2, (0,"a"):1,
	   (1,"a"):1, (1,"b"):3,
	   (2,"a"):1, (2,"b"):2,
	   (3,"a"):3, (3,"b"):3},
	   0,
	   {0,1,2})

if __name__ == "__main__":
    input_string = "aabba"  # replace with your input string
    print(D0.run(input_string))