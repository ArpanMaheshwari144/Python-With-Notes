sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))
sub3 = int(input("Enter marks of subject 3: "))

total = ((sub1 + sub2 + sub3)*100)/300

if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail because you have less than 33% in one of the subject")
elif(total<40):
    print("You are fail because your total percentage is", total, "which is less than 40")
else:
    print("Congratulations! You passed the exam with total percentage of", total)
