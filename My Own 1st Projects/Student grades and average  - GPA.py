### Dec. 30, 2021 - Approaching New Year's Day !!! ###
### This scripts aims to read 10 earned grades of a student and, at the end, calculate the Grade Point Average for this student 
### In Brazil, the usual form of GPA is based on a scale ranging from 0.0, which means 0%, up to 10.0, which in turn represents 100%
### of the objectives expected from a student during a certain evaluation. Usually, a GPA equal or greater than 7.0 (70%)
### is a good mark and enables the student to go ahead through the next levels of his/hers education. 

### The idea for this program can be found at page 10 of the syllabus "Algoritmo - 4ª etapa" edited by Uniasselvi.

### Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil ###

student_data=[]
student_name = input("Enter student name: ")
student_data.append(student_name)

i = 1
while i <= 10:
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

print("\nStudent name: ", student_data[0])
sum_grades = 0
i = 1
while i <= 10:
    print("Grade #", i, ":", student_data[i])
    sum_grades = sum_grades + student_data[i]
    i+=1
print("\n" + student_data[0] + "'s GPA is", sum_grades/10)

if (sum_grades/10) >= 7:
    print("\nCongratulations! Good Job ! See you at the next class. Bring your new books !!")
else:
    print("\nSorry! You need to review your lessons and apply to a new examination.")
print("\n\n### Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil ###")