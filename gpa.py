n = int(input("Give your marks: "))

if 80 <= n <= 100:
    print("A+")
elif 70 <= n <= 79:
    print("A")
elif 60 <= n <= 69:
    print("A-")
elif 50 <= n <= 59:
    print("B")
elif 40 <= n <= 49:
    print("C")
elif 33 <= n <= 39:
    print("D")
else:
    print("F")