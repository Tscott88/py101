# Write two different ways to remove all of the elements from the following list:

numbers1 = [1, 2, 3, 4]
numbers2 = [1, 2, 3, 4]

numbers1.clear()
print(numbers1)

while numbers2:
    numbers2.pop()

print(numbers2)