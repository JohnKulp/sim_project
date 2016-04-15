import numpy as np

class Faculty():

	def __init__(self, ID=None, courses=[], difficulty=0.0):
		self.ID = ID
		self.courses = courses		# a list of course objects
		self.difficulty = difficulty

	def add_course(self, course):
		if course.course_num >= 0:
			self.courses.append(course)
			return True
		return False

	def set_difficulty(self):
		# some calculations here
