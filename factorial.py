m = int(input("Enter a number: "))
def factorial(m):
    if m == 0 or m == 1:
        return 1
    else:
        return factorial(m-1)*m
print(f"factorial of {m} is {factorial(m)}")
        