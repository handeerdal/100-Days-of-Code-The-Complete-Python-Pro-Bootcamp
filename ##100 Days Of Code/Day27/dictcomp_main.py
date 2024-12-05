students=['Jahn','Jack','Helena']
import random

studentdict={ student:random.randint(1,100) for student in students}
print(studentdict)

passedstudents={student:grade for (student,grade) in studentdict.items() if grade>50     }

print(passedstudents)