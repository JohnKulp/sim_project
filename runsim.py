import student
import record
import faculty
import course


import random
import scipy.stats as st
import sys


PASSFAIL = True
dropouts = []

def generate_core_courses(num_core):
	courses = []

	for i in range(num_core):
		courses.append(Course(i))

	return courses


def generate_students(num_to_generate):
	
	students = []

	for i in range(num_to_generate):
		students.append(Student(skill_level = random.random()))



def grading(difficulty, passfail = True):
	if passfail:
		return 1.0 if random.random() >= (1-difficulty) else 0.0
	else:
		grade = random.random()
		return grade if grade >= () (1-difficulty) else 0.0

# a term is a list of courses
def update_students_with_new_grades(term):
	for course in term:
		for student in course.students:
			grade = grading(course.difficulty, PASSFAIL)
			student.add_course(course.classID,grade)


def find_leaving_students(students):
	new_grads_or_dropouts = []
	for student in students:
		if completed_core_classes(student):
			graduates.append(student)
			new_grads_or_dropouts.append(student)
		elif student.classes_failed > 15:
			dropouts.append(student)
			new_grads_or_dropouts.append(student)

	for student in new_grads_or_dropouts:
		students.remove(student)


# term is a list of courses for the semester
def find_plans_to_retake(term):
	for course in term:
		for student in course.students:
			# this key should exist by the time this is called
			if student.course_transcript[course.classID] == 0:
				student.plan_to_retake.append(course.classID)


def runloop(students, term, num_incoming):
	new_students = generate_students(num_incoming)

	#this causes a deep change in the object instead of changing list pointer
	number_new = len(new_students)
	for i in range(number_new):
		students.append(new_students.remove())

	populate_courses_with_students(term, students)

	update_students_with_new_grades(term)

	find_leaving_students(students)
	find_plans_to_retake(term)




if __name__ == "__main__":

	if len(sys.argv) != 2:
		print("run with number of iterations as the only argument")
		
	else:

		courses = generate_courses(20)

		num_iterations = int(sys.argv[1])

		for i in range(num_iterations):
			runloop()
