
def frequency_counter(numbers):

    # Create an empty dictionary
    frequency = {}

    # Loop through the list
    for num in numbers:

        # Check if number exists as a key
        if num in frequency:

            # Increase its value by 1
            frequency[num] = frequency[num] + 1

        else:

            # Add a new key with value 1
            frequency[num] = 1

    return frequency


numbers = [1, 2, 2, 3, 3, 3, 4]

result = frequency_counter(numbers)

print(result)



