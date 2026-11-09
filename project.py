class Student_Registration_System(Exception):
    pass
try:
    student_id=input('Enter a Student ID:')
    name=input('Enter a Name:')
    age=int(input('Enter Age:'))
    email=input('Enter a Email:')
    mobile_number=input('Enter Mobile Number:')
    course=input('Enter a Course Name:')
    password=input('Enter a Password:')

    if len(student_id) != 3 or not student_id.isdigit():
        raise Student_Registration_System('Student id must excetly 3 characters and it contains only digits')
    if len(name) < 4 or not name.isalpha():
        raise Student_Registration_System('Name must be atleast 4 characters and it contains only alphabetics')
    if age < 15 or age > 25:
        raise Student_Registration_System('age must be in between 15 to 25')
    if not '@' in email or not email.endswith('.com'):
        raise Student_Registration_System('Email must contains @ and end with .com')
    if len(mobile_number) !=10 or not mobile_number.isdigit():
        raise Student_Registration_System('mobile Number must contains excatly 10 digits')
    if not course.isalpha() or not course.isupper():
        raise Student_Registration_System('Course must be in capital letters')
    if len(password) < 8:
        raise Student_Registration_System('Password must contain at least 8 characters')
    if not any (ch.isupper() for ch in password):
        raise Student_Registration_System('Password must contain at least one upper case letter')
    if not any (ch.islower() for ch in password):
        raise Student_Registration_System('Password must contain at least one lower case letter')
    if not any (ch.isdigit() for ch in password):
        raise Student_Registration_System('Password must contain at least one digit')
    Special="'!@#$%^&*()<>.,;:?"
    if not any(ch in Special for ch in password):
        raise Student_Registration_System('Password must contain at least one special character')
    
except Student_Registration_System as e:
    print(e)
except ValueError as e:
    print(e)
else:
    print('student registration system successfully')
    
finally:
    print('Student Registration System Completed')