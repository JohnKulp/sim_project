import numpy as np

class Course():

	def __init__(self, class_size=0, students=[], difficulty=0):
		self.class_size = class_size
		self.students = students			#students is a list of Student IDs
		self.difficulty = difficulty
