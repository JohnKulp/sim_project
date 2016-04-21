#takes the number of semester from graduates and returns an average
def get_average_time_in_system(student_list):
	total_semesters=0
	average_semester=0
	for student in student_list:
		total_semesters+=student.semesters_completed
	if total_semesters!=0:
		average_semester=double(total_semesters)/len(student_list)		
	return average_semester

#takes number of classes failed from graduates and returns an average
def get_average_classes_failed(student_list):
	total_failed=0
	average_failed=0
	for student in student_list:
		total_failed+=len(student_list.classes_failed)
	if total_failed!=0:
		average_failed=double(total_failed)/len(student_list)		
	return average_failed
#takes a list of students and returns a dictionary of the classes failed + how many students failed it
def get_number_class_failures(student_list):
	class_number_failed{}
	for student in student_list:
		for course, failed_number in student_list.classes_failed:
			if class_number_failed.setdefault(course, none) != none:
				class_number_failed[course]+=failed_number
			else: 
				class_number_failed[course]=0
	return class_number_failed

		"""
		if "401" in student_list.classes_failed:
			class_number_failed["401"] += student_list.classes_failed["401"]
		if "441" in student_list.classes_failed:
			class_number_failed["441"] += student_list.classes_failed["401"]	
		if "1502" in student_list.classes_failed:
			class_number_failed["1502"] += student_list.classes_failed["401"]
		if "1501" in student_list.classes_failed
			class_number_failed["401"] += student_list.classes_failed["401"]
		"""		