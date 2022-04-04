import time
start_time = time.time()
grades=[4,73,67,38,33]
# def gradingStudents(grades):
for grade in grades:
    if grade >=38 and (grade % 5>2):
        grade=grade-grade%5+5
    print(grade)
       

print("Process finished --- %s seconds ---" % (time.time() - start_time))