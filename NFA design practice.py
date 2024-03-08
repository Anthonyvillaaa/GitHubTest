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


N0 = NFA({0,1,2},
	  {'_', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'},
	  {(0,'1'):{1}, (0,'2'):{1}, (0,'3'):{1}, (0,'4'):{1}, (0,'5'):{1}, (0,'6'):{1}, (0,'7'):{1}, (0,'8'):{1}, (0,'9'):{1},
	(1,'_'):{2}, (1, '0'):{1}, (1,'1'):{1}, (1,'2'):{1}, (1,'3'):{1}, (1,'4'):{1}, (1,'5'):{1}, (1,'6'):{1}, (1,'7'):{1}, (1,'8'):{1}, (1,'9'):{1},
	(2,'0'):{3,1}, (2,'1'):{3,1}, (2,'2'):{3,1}, (2,'3'):{3,1}, (2,'4'):{3,1}, (2,'5'):{3,1}, (2,'6'):{3,1}, (2,'7'):{3,1}, (2,'8'):{3,1}, (2,'9'):{3,1},
	(3,'0'):{3,1}, (3,'1'):{3,1}, (3,'2'):{3,1}, (3,'3'):{3,1}, (3,'4'):{3,1}, (3,'5'):{3,1}, (3,'6'):{3,1}, (3,'7'):{3,1}, (3,'8'):{3,1}, (3,'9'):{3,1},

	(0,'0'):{4},(4,'_'):{5},(5,'0'):{6,4},(6,'0'):{6,4}},

	  {0},
	  {1,3,6})
	
	

if __name__ == "__main__":
    input_string = input("Please enter valid decimal integer: ")
    print(N0.run(input_string))
