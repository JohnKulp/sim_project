import numpy as np

class Student():

	def __init__(self, courses=[], semesters_completed=0, GPA=None, ):
		self.GPA = GPA
		self.courses = courses
		self.semesters_completed = semesters_completed

	def add_course(self, course_ID, grade_received):
		if course_ID in self.courses[0]:
			return retake_course(self, course_ID, grade_received)

		self.courses[0].append(course_ID)
		self.courses[1].append(grade_received)

		self.classes_taken += 1

		if grade_received < 72.5:
			self.classes_failed += 1

		return True

	def retake_course(self, course_ID, grade_received):
		self.classes_taken += 1

		for index in range(len(self.courses[0])):
			if self.courses[0][index] == course_ID:
				self.courses[1][index] = grade_received
				calculate_GPA(self)
				return True

		return False

	def calculate_GPA(self):
		self.GPA = np.average(self.courses[1])
		return self.GPA

	def pass_rate(self):
		return 1-float(self.classes_failed)/self.classes_taken