#wih statement
with open("example.txt", "w") as file:
    file.write("Hello Python")

    #next and iter
    # define a list
my_list = [4, 7, 0]

# create an iterator from the list
iterator = iter(my_list)

# get the first element of the iterator
print(next(iterator))  # prints 4

# get the second element of the iterator
print(next(iterator))  # prints 7

# get the third element of the iterator
print(next(iterator))  # prints 0


#genrator using yield
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

print(next(gen))
print(next(gen))
print(next(gen))

#gen using Loop
def numbers():
    yield 10
    yield 20
    yield 30
    yield 40

for num in numbers():
    print(num)


#gen with range()
    def count():
        for i in range(1, 6):
           yield i

for number in count():
    print(number)


#using return
def normal_function():
    return 1
    return 2

print(normal_function())    

