# range function
for i in range(8):
    print(i, end=" ")

for i in range(5, 10):
    print(i, end=" ")
    
for i in range(2, 10, 2):
    print(i, end="")
    
for i in range(-10, -100, -20):
    print(i, end=" ")

a = ["I", "am", "a", "intelligent", "man"]
for i in range(len(a)):
    print(i, a[i])
