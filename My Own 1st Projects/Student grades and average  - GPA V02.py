### Dec. 31, 2021 - Approaching New Year's Day !!! ###
### This script aims to read a given quantity of grades achieved by a student and, at the end, calculate the Grade Point Average for this student.
### In Brazil, the usual form of GPA is based on a scale ranging from 0.0, which means 0%, up to 10.0, which in turn represents 100%
### of the objectives expected from a student during a certain evaluation. Usually, a GPA equal or greater than 7.0 (70%)
### is a good mark and enables the student to go ahead through the next levels of his/her education. 

### Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil ###

student_data=[]
student_1st_name = input("Enter student first name: ")
student_1st_name = student_1st_name.upper()
student_data.append(student_1st_name)
student_2nd_name = input("Enter student second name: ")
student_2nd_name = student_2nd_name.upper()
student_data.append(student_2nd_name)

while True:
    try:
        qty_grades = input("Quantity of grades: ")
        qty_grades = int(qty_grades)
    except:
        continue
    
    if qty_grades >= 1 and qty_grades <=10:
        break
    else:
        continue

i = 1
while i <= qty_grades:
    try:
        print("Enter grade #", i, ": ", end="")
        grade = float(input())
        if grade < 0 or grade > 10:
            print("Invalid grade ! A grade ranges from 0.0 up to 10.0. Check it once again, please.")
            continue  
    except:
        print("Invalid grade ! A grade ranges from 0.0 up to 10.0. Check it once again, please.")
        continue
    student_data.append(grade)
    i+=1


print("\n\n    **** Student data ****    ")

print("\nStudent name: ", student_data[0], student_data[1])
sum_grades = 0
i = 2
while i <= (qty_grades+1):
    print("Grade #", i-1, ":", student_data[i])
    sum_grades = sum_grades + student_data[i]
    i+=1
print("\n" + student_data[0] + "'s GPA is", sum_grades/qty_grades)

if (sum_grades/qty_grades) >= 7:
    print("\nCongratulations! Good Job ! See you for the next class. Bring your new books !!")
else:
    print("\nSorry! You need to review your lessons and apply to a new examination.")
print("\n\n### Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil ###")


