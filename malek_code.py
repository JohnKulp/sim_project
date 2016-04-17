import operator
import random 
def populate_courses(term,students):
	students.sort(key=operator.attrgetter(students.credits), reverse=True)
	for student in students:
		courses_taken=[]
		for courseID in student.plan_to_retake:
			for i in range(len(term)):
				if courseID == term[i].classID:
					if(term[i].class_size>len(term[i].students)):
						courses_taken.append(courseID)
						term[i].students.append(student)
						student.plan_to_retake.remove(courseID)
						if courses_taken == 3:
							break					
		random.shuffle(term)
		for course in term:
			if course.courseID not in courses_taken and course.courseID not in student.course_transcript and course.class_size>len(course.students):					
				courses_taken.append(courseID)
				course.students.append(student)
				if courses_taken == 3:
					break
			
