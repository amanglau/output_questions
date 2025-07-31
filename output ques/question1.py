x = (int(input()))
y = int(input())

if x > y:
    if y > 0:
        z = x // y 
    else:
        z = x * y
else:
    z = 0

print(z)
