student = {
    'Name': 'Ford Prefect',
    'Gender': 'Male',
    'Occupation': 'Researcher',
    'Home Planet': 'Betelgeuse Seven'
}
student.setdefault('Phone', 813745638)
#print(student['Name'])
student['Age'] = 33
#print(student)
for i,j in zip(student.keys(), student.values()):
    print(i,j)
