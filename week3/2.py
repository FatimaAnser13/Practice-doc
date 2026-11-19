#largest number
numbers = [10, 25, 5, 40, 15, 30]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number:", largest)


#Prime number
num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")



#revese string
text = "helloworld"

reverse_text = text[::-1]

print(reverse_text)