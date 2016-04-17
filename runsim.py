import student
import record
import faculty
import course


import random
import scipy.stats as st
import sys


PASSFAIL = True

def generate_core_courses(num_core):
	courses = []

	for i in range(num_core):
		courses.append(Course(i, class_size = 30))

	return courses


def generate_students(num_to_generate):
	
	students = []

	for i in range(num_to_generate):
		students.append(Student(skill_level = random.random()))


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


def runloop(students, term, num_incoming):
	new_students = generate_students(num_incoming)

	#this causes a deep change in the object instead of changing list pointer
	number_new = len(new_students)
	for i in range(number_new):
		students.append(new_students.remove())

	populate_courses_with_students(term, students)

	generate_student_records(term)

	find_dropouts(students)
	find_graduates(students)
	find_plans_to_retake(students)




if __name__ == "__main__":

	if len(sys.argv) != 2:
		print("run with number of iterations as the only argument")
		
	else:

		courses = generate_courses(20)

		num_iterations = int(sys.argv[1])

		for i in range(num_iterations):
			runloop()
