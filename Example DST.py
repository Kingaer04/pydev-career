from pprint import pprint as prt


student = {}
student['Daniel'] = {'Name': 'Anifowoshe Daniel',
                     'Maric Num': '20/1011',
                     'Department': 'Computer Science',
                     'Level': '300'}
student['Michael'] = {'Name': 'Ibrahim Michael',
                      'Matric Num': '21/0611',
                      'Department': 'Computer Science',
                      'Level': '300'}
prt(student['Daniel']['Level'])
