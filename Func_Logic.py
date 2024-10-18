def findmax(a, b):
    """
    This function is used find max of two numbers
    """
    if a > b:
        return a
    else:
        return b


n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
result = findmax(n1, n2)
print(result)
