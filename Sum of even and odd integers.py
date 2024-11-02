num = input("Input a set of integers separated by spaces: ")

integers = num.split()
even = 0
odd = 0

for num in integers:
    number = int(num)
    if number % 2 == 0:
       even += number
    else:
        odd += number

print("Sum of even integers:", even)
print("Sum of odd integers:", odd)
