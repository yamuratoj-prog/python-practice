numbers = [4, 7, 12, 3, 18, 9, 21, 6, 15, 10]
evens = [number for number in numbers if number % 2 == 0]
print(evens)
total = 0
for n in numbers:
    total += n
print(total)
print(max(numbers))