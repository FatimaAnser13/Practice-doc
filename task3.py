#Print 1 to 20, but print “Fizz” for multiples of 3, “Buzz” for multiples of 5, and “FizzBuzz” for multiples of both.
for i in range(1,21):
    if i % 3 ==0 and i % 5 ==0:
        print("FizzBuzz")
    elif i % 3 ==0:
        print("Fizz")
    elif i % 5 ==0:
            print("Buzz")
    else:
         print(i)
    
