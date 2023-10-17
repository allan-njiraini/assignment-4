# number = int((input('Enter Number:')))

#if number > 0:
#    print("positive")
#elif number < 0:
#    print("negative")
#else:
#    print("zero")

# Function to calculate the grade based on the average total marks
def calculate_grade(average_total_marks):
    if 71 <= average_total_marks <= 100:
        return "A"
    elif 51 <= average_total_marks < 70:
        print ("B")
    elif 31 <= average_total_marks < 50:
        print ("C")
    elif 0 <= average_total_marks < 30:
        print ("D")
    else :100 < average_total_marks < 0
    return "unrecognized marks/avg"
    

# Input the marks for each subject
math = float(input("Enter marks for Maths: "))
physics = float(input("Enter marks for Physics: "))
geography = float(input("Enter marks for Geography: "))
chemistry = float(input("Enter marks for Chemistry: "))

# Calculate the average total marks
average_total_marks = (math + physics + geography + chemistry) / 4

# Calculate the grade
grade = calculate_grade(average_total_marks)

# Display the results
print(f"Average Total Marks: {average_total_marks}")
print(f"Grade: {grade}")


