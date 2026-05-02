numbers = [1, 3, 2 ,4, 3, 4, 5, 5,]
new = []
for number in numbers:
    if number not in new:
        new.append(number)
print(new)