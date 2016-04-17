import random

import student

def generate_students(num_to_generate):
	
	students = []

	for i in range(num_to_generate):
		students.append(Student(skill_level = random.random()))