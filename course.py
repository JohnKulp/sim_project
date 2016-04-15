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

	def add_student(self, student_ID):
		if self.spots_left > 0:
			if student_ID != None and student_ID >= 0:
				self.students.append(student_ID)
				self.spots_left -= 1
				return 1
		return 0	

	def add_students(self, student_ID_list):
		students_added = 0
		if len(student_ID_list) > 0:
			for student_ID in student_ID_list:
				students_added += add_student(self, student_ID)
		return students_added

	def set_faculty(self, faculty_ID):
		if faculty_ID >= 0:
			self.faculty_ID = faculty_ID

	def set_term(self, term_ID):
		if term_ID >= 0:
			self.term_ID = term_ID

	def set_success_rate(self, success_rate):
		# some calculations here
		# how do we want to calculate this since we have no data?