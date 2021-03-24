# Write a complete program that prompts the user for a student’s status and grade 	point average ( GPA ) and then determines whether or not the student should be 	placed on the Dean’s list.  Assume that a student is placed on the Dean’s list 	when he / she has full - time status and a GPA of at least 3.50 .  Part - time 	students cannot be placed on the Dean’s list regardless of their GPA.

status = input("Please enter your status: \n")
gpa = input(float("Please enter you GPA: \n"))

if(status == "Full Time" and gpa >= 3.50):
    print("Congrats! You made the dean's list.")
elif(status == "Part Time"):
    print("Part time students are not eligible")
else:
    print("Better luck next semester!")
