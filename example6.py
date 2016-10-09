def Name(name):
	print("Hi! "+name)

students = ["York","Jerry","Frank"]

i=0

for student  in students:
	i=i+1
	Name(student)
	if i != len(students):
		print("Next")
	else:
		print("Finish")
