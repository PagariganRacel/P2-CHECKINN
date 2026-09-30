num_student = int(input("How Many Students: "))
def status(stts):
    if stts >= 90:
        status = "Excellent"
    elif stts >= 80:
        status = "VeryGood"
    elif stts >= 75:
        status = "Passed"
    else:
        status = "Failed"
    return status

i = 1
for i in range(1, num_student + 1):
    print("")
    print("Student" + str(i))
    name = input("Enter Your Name:")
    score1 = int(input("ACTIVITY 1: "))
    score2 = int(input("ACTIVITY 2: "))
    score3 = int(input("ACTIVITY 3: "))
    total = score1 + score2 + score3
    average = total / 3
    print("Average:", str(average))
    print("Status:", status(average))