#if/elif/else. Write a grading program:
#90 and above → A
#80–89 → B
#70–79 → C
#Below 70 → F

score = float(input("enter your score:"))
if score >=90:
    print("A")
elif score >=80:
    print("B")
elif score >=70:
    print("C")
else:
    print("F")

