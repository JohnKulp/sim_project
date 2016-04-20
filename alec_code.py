
def populate_courses_with_students(term,students):
	required = []
	elecitves = []
	for course in term:
		if course.course_id <= 400:
			electives.append(course)
		else:
			required.append(electives)

	students.sort(key = lambda x: len(x.course_transcript), reverse=True)
	for student in students:
		courses_taken=[]
		max_courses = 2 + (1 if random.random() < student.skill_level else 0)
		#try to retake courses the student plans to retake first
		for course_id in student.plan_to_retake:
			if course_id <= 400:
				# elective
				for i in range(len(electives)):
					if course_id == electives[i].course_id and len(courses_taken) < max_courses:
						if electives[i].class_size > len(electives[i].students):
							courses_taken.append(course_id)
							electives[i].students.append(student)
			else:
				# required
				for i in range(len(required)):
					if course_id == required[i].course_id and len(courses_taken) < max_courses:
						if required[i].class_size > len(required[i].students):
							courses_taken.append(course_id)
							required[i].students.append(student)
							if len(courses_taken) == max_courses:
								continue

		# remove the courses we just added from plan_to_retake	
		for course_id in courses_taken:
			student.plan_to_retake.remove(course_id)

		required.sort(key = lambda x: x.course_id)
		random.shuffle(electives)
		for course in required:
			if len(courses_taken) >= max_courses:
				break

			if course.course_id not in courses_taken and course.course_id not in student.course_transcript \
					and course.class_size >= len(course.students):
				courses_taken.append(course.course_id)
				course.students.append(student)

		for course in electives:
			if len(courses_taken) >= max_courses:
				break

			if course.course_id not in courses_taken and course.course_id not in student.course_transcript \
					and course.class_size>=len(course.students):
				courses_taken.append(course.course_id)
				course.students.append(student)
