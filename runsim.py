from Student import Student
from Faculty import Faculty
from Course import Course

import operator
import random
import scipy.stats as st
import sys


global passfail
global dropouts
global graduates 

def generate_core_courses(num_core):
	courses = []

	for i in range(num_core):
		courses.append(Course(i))

	return courses


def generate_students(num_to_generate):
	
	students = []

	for i in range(num_to_generate):
		students.append(Student(skill_level = random.random()))

	return students



def grading(difficulty, passfail = True):
	if passfail:
		return 1.0 if random.random() >= (1-difficulty) else 0.0
	else:
		grade = random.random()
		return grade if grade >= () (1-difficulty) else 0.0

# a term is a list of courses
def update_students_with_new_grades(term):
	global passfail
	for course in term:
		for student in course.students:
			grade = grading(course.difficulty, passfail)
			student.add_course_grade(course.course_id,grade)


def sort_students(student1, student2):
	credits1 = len(student1.course_transcript)
	credits2 = len(student2.course_transcript)
	if credits1 > credits2:
		return -1
	elif credits1 == credits2:
		return 0
	else:
		return 1

def populate_courses_with_students(term,students):
	students.sort(key = lambda x: len(x.course_transcript), reverse=True)
	for student in students:
		courses_taken=[]
		for course_id in student.plan_to_retake:
			for i in range(len(term)):
				if course_id == term[i].course_id:
					if(term[i].class_size>len(term[i].students)):
						courses_taken.append(course_id)
						term[i].students.append(student)
						student.plan_to_retake.remove(course_id)
						if courses_taken == 3:
							break					
		random.shuffle(term)
		for course in term:
			if course.course_id not in courses_taken and course.course_id not in student.course_transcript and course.class_size>len(course.students):					
				courses_taken.append(course.course_id)
				course.students.append(student)
				if courses_taken == 3:
					break

def completed_core_classes(student):
	return len(student.course_transcript) >= 20

def find_leaving_students(students):
	global graduates
	global dropouts
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
			if student.course_transcript[course.course_id] == 0:
				student.plan_to_retake.append(course.course_id)


def runloop(students, term, num_incoming):
	new_students = generate_students(num_incoming)

	#this causes a deep change in the object instead of changing list pointer
	number_new = len(new_students)
	for i in range(number_new):
		students.append(new_students.pop())

	populate_courses_with_students(term, students)

	update_students_with_new_grades(term)

	find_leaving_students(students)
	find_plans_to_retake(term)

	return students



if __name__ == "__main__":

	global passfail
	global dropouts
	global graduates

	passfail = True
	dropouts = []
	graduates = []

	if len(sys.argv) != 2:
		print("run with number of iterations as the only argument")
		
	else:

		courses = generate_core_courses(20)

		num_iterations = int(sys.argv[1])

		students = []

		for i in range(num_iterations):
			students += runloop(students, courses, 300)

		print("at the end of the simulation, there were {} dropouts and {} graduates".format(len(dropouts), len(graduates)))
		print("some sample GPAs were: ")
		for i in range(10):
			print(graduates[i].course_transcript)
