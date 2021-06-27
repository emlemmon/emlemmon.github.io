numbers = [12, 18, 128, 48, 2348, 21, 18, 3, 2, 42, 96, 11, 42, 12, 18]

numbers.insert(0, 5)
print(numbers)

numbers.remove(2348)
print(numbers)

numbers2 = [22, 33, 44, 55, 66]
numbers.extend(numbers2)
print(numbers)

numbers.sort()
print(numbers)

numbers.sort(reverse = True)
print(numbers)


print(numbers.count(12))
print(numbers.index(96))
print(len(numbers))
print(numbers[:10])
print(numbers[10:])
print(numbers[::2])
print(numbers[-5:])