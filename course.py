import numpy as np

class Course():

	def __init__(self, course_num=-1, class_size=0, students=[], faculty_ID=None, term_ID=0, success_rate=0.0):
		self.course_num = course_num
		self.class_size = class_size
		self.slots_left = class_size
		self.students = students			#students is a list of Student IDs
		self.faculty_ID = faculty_ID
		self.term_ID = term_ID
		self.success_rate = success_rate

	def set_success_rate(self, success_rate):
		pass
		# some calculations here
		# how do we want to calculate this since we have no data?