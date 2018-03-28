grades=int(input("How many grades would you like to input?"))
grade_list= []
grade_average = 0
for i in range(grades):
    print ("What was your grade?")
    entered_vari=int(input())
    grade_list.append(entered_vari)
    grade_average = grade_average + entered_vari
print grade_list
a= grade_average
a = a/grades
print a
if a >=90:
    print ("You have an A")
elif a>=80 and a<90:
    print "You have a B"
elif a>=70 and a<80:
    print "You have a C"
elif a>=60 and a<70:
    print "You have a D"
else:
    print "!!You Are Failing!!"
