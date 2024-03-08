class NFA:
	def __init__(self, Q, Sigma, Delta, S, F):
		self.Q = Q	# Set of states
		self.Sigma = Sigma	# Alphabet
		self.Delta = Delta	# Transition function as a dictionary
		self.S = S	# Set of Start states
		self.F = F	# Set of accept states

	def __repr__(self):
		return f"DFA ({self.Q}, \n\t{self.Sigma}, \n\t{self.delta}, \n\t{self.S}, \n\t{self.F})"

	def do_delta(self,q,x):
		try:
			return self.Delta[(q,x)]
		except KeyError:
			return set({})
	

	def run (self,w) :
		P = self.S
		while w != "":
			Pnew = set({})
			for q in P:
				Pnew = Pnew or self.do_delta(q,w[0])
			w = w[1:]
			P = Pnew
		return (P & self.F) != set({})


N0 = NFA({0,1,2},{"0","1"}, 
	 {(0, "1"):{1},(1,"0"):{1,2},(1,"1"):{1}},
	{0}, 
	{2})

if __name__ == "__main__":
    input_string = "1001"  # replace with your input string
    print(N0.run(input_string))
