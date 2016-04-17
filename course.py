import numpy as np

class Course():

	#term is 1 for odd, 2 for even, 3 for all
	def __init__(self, classID, class_size=0, students=[], difficulty=0, term=3):
		self.classID = classID
		self.class_size = class_size
		self.students = students			#students is a list of Student IDs
		self.difficulty = difficulty
		self.term = term
