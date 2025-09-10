score = int(input("Enter the score: "))

if score > 100:
    print("Invalid score")
    exit()

if score >= 90:
    grade = "A"
elif score >= 80 and score <= 89:
    grade = "B"
elif score >= 70 and score <= 79:
    grade = "C"
elif score >= 60 and score <= 69:
    grade = "D"
else:
    grade = "F"


print(f"Grade of the student is {grade}")