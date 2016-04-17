import numpy as np

class Student():

	def __init__(self, ID=None, GPA=0.0, courses=[[],[]], classes_taken=0, classes_failed=0, semesters_completed=0, dropped_out=False):
		self.ID = ID
		self.GPA = GPA
		self.courses = courses
		self.classes_taken = classes_taken
		self.classes_failed = classes_failed
		self.semesters_completed = semesters_completed
		self.dropped_out = dropped_out

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

	def finish_semester(self):
		self.semesters_completed += 1

	def drop_out(self):
		self.dropped_out = True

	def pass_rate(self):
		return 1-float(self.classes_failed)/self.classes_taken