#for loop. Print the multiplication table of a number the user enters:
#5 x 1 = 5
#5 x 2 = 10

num = int(input("enter a number:"))
for i in range(1,11):
    print(f"{num} x {i} ={num * i}")
    