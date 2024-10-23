#Question 3
# Using loop of your choice, WITI  has tasked you to automate a simple grading system. 
# As a python student, write a program using functions and conditions to display the grades that 
# the students will be receiving. 
# The grades are:
# 90% - 100%  Grade is A
# 80% - 89% Grade is   B
# 70% - 79% Grade is   C                                                        
# 60% - 69%  Grade is  D                  
# 50% - 59%  Grade is  E  
# < 50%                Fail 


def grading():
    mark = int(input("Enter the marks: "))
    if 90 <= mark <= 100:
        print("The grade is A")
    elif 80 <= mark <= 89:
        print("The grade is B")
    elif 70 <= mark <= 79:
        print("The grade is C")
    elif 60 <= mark <= 69:
        print("The grade is D")
    elif 50<= mark <= 59:
        print("The grade is E")
    else:
        print("fail")
grading()
