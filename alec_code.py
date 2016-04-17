import student
import record
import faculty
import course
import random
import scipy.stats as st

PASSFAIL = True

# a term is a list of courses
def term_occur(term):
	for course in term:
		for student in course.students:
			grade = grading(course.difficulty, PASSFAIL)
			student.add_course(course.classID,grade)

def grading(difficulty, passfail = True):
	if passfail:
		return 1.0 if random.random() >= (1-difficulty) else 0.0
	else:
		grade = random.random()
		return grade if grade >= () (1-difficulty) else 0.0