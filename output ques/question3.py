n = 2

if n == 1:
    print("One")
elif n == 2:
    n = n + 1
    print("Two")
    if n == 3:
        print("Three")
        print("Other")
elif n == 3:
    print("Three")
    print("Other")
else:
    print("Other")
