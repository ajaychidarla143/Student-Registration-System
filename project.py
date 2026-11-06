
class Student_Registration_system(Exception):
    pass
try:
    student_id=input("Enter a Student Id:")
    name=input("Enter a name:")
    age=int(input('Enter age:'))
    mobile_number=input("Enter Mobile number:")
    password=input('Enter password:')

    if len(student_id) < 3 or not student_id.isdigit():
        raise Student_Registration_system('Student id must above 3 characters and it contains only digits')
    if len(name) < 4 or not name.isalpha():
        raise Student_Registration_system('name must be above 4 characters and it contains only letters')
    if age < 15 or age > 28 :
        raise Student_Registration_system('age must be between 15 to 28')
    if len(mobile_number) !=10 or not mobile_number.isdigit():
        raise Student_Registration_system('Mobile number must be excatly 10 digits')
    if len(password) < 8:
        raise Student_Registration_system('Password must be above 8 characters')
    if not any (ch.isupper() for ch in password):
        raise Student_Registration_system('Password must contain at least one upper case letter')
    if not any (ch.islower() for ch in password):
        raise Student_Registration_system('Password must contain at least one lower case letter')
    if not any (ch.isdigit() for ch in password):
        raise Student_Registration_system('Password must contain at least one digit')
    special="'!@#$%^&*()_+/.,?><[]:;"
    if not any(ch in special for ch in password):
        raise Student_Registration_system('Password must contain at least one special character')

except Student_Registration_system as e:
    print(e)
except ValueError as e:
    print(e)
else:
    print('student Registration system sucessfully')

finally:
    print('student registration system completed')
    