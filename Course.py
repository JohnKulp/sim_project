import numpy as np
import math

class Course():

	#term is 1 for odd, 2 for even, 3 for all
	def __init__(self, course_id, class_size=float('inf'), students=[], difficulty=0, term=3):
		self.course_id = course_id
		self.class_size = class_size
		self.students = students			#students is a list of Student IDs
		self.difficulty = difficulty
		self.term = term
