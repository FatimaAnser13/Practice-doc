1.#Assignment. Start with x = 10, then apply += 5, -= 3, and *= 2, printing after each step.
x = 10
x += 5
print(x)  # 15
x -= 3
print(x)  # 12
x *= 2
print(x)  # 24


2.#Comparison. True or False?
print(5 > 3) # true 
print(5 == 5.0) # true  
print(10 != 10) # false 
print("a" == "A") # false



3.#Logical. Predict each result.
age = 20
has_id = True
print(age >= 18 and has_id) #True
print(age < 18 or has_id) #True 
print(not has_id) #False


4.#Membership and identity.
fruits = ["apple", "banana", "mango"]
print("apple" in fruits) #True
print("grape" not in fruits) #True


a = [1, 2]
b = [1, 2]
print(a == b)
print(a is b)
#Explain why a == b and a is b give different answers.
(a == b) #True (== compare values) Both lists contain the same elements values are in same order 
(a is b) #False (is checks identity) both lists contain the same elements, they are two separate objects stored seperatey.


#Bitwise. Predict 
print(5 & 3) #1
print(5 | 3) #7
