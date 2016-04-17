import course
import faculty
import record
import student

import sys


def runloop():
	pass

	

if __name__ == "__main__":

	if len(sys.argv) != 2:
		print("run with number of iterations as the only argument")
		
	else:
		num_iterations = int(sys.argv[1])

		for i in range(num_iterations):
			runloop()
