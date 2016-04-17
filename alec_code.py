import student
import record
import faculty
import course
import random


# term is a list of courses for the semester
def find_plans_to_retake(term):
	for course in term:
		for student in course.students:
			# this key should exist by the time this is called
			if student.course_transcript[course.classID] == 0:
				student.plan_to_retake.append(course.classID)