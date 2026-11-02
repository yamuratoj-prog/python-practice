text = input("Enter a string: ")
vowels = "аеёиоуыэюяaeiou"
count = 0

for ch in text.lower():
    if ch in vowels:
        count +=1

print(text[::-1])
print(count)