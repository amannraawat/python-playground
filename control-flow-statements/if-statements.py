##### if statement
x = int(input("Enter a number: "))
if x < 0:
    x = 0
    print("Negative number changed to zero")
    print(x)
elif x == 0:
    print("Zero")
elif x == 1:
    print("One")
else:
    print("Greater than one")
