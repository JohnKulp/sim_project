import course
import faculty
import record
import student

import sys


def generate_courses(num_core):
	courses = []

	for i in range(num_core):
		courses.append(Course(i, class_size = 30))

	return courses


def runloop():
	pass



if __name__ == "__main__":

	if len(sys.argv) != 2:
		print("run with number of iterations as the only argument")
		
	else:

		courses = generate_courses(20)

		num_iterations = int(sys.argv[1])

		for i in range(num_iterations):
			runloop()
