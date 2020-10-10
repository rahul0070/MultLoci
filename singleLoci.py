import parameters

class Population:
	def __init__(self):
		self.allele_A = 0
		self.allele_D = 0

	def alleleFrequencies(self):
		print('A: ', self.allele_A, '|| D: ', self.allele_D)

class SingleLoci:
	def __init__(self):
		self.p1 = Population()
		self.p2 = Population()
		self.iterations = parameters.iterations
		self.size = parameters.n
		self.createPopulation()

	def createPopulation(self):
		# Begining case (t = 0)
		self.p1.allele_A = self.size
		self.p1.allele_D = 0

		self.p2.allele_A = self.size
		self.p2.allele_D = 0


	def induceMutation(self):
		pass

	def migration(self):
		pass

	def selection(self):
		pass

	def run(self):
		self.induceMutation()

		for i in range(self.iterations):
			self.migration()
			self.selection()

		self.p1.alleleFrequencies()
		self.p2.alleleFrequencies()
	