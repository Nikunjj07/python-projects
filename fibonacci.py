a = 0
b = 1
count = 0
terms = int(input("Enter the number of terms for fibonacci: "))
while count<terms:
    print(a, sep=',')
    c = a+b
    a = b
    b = c
    count += 1