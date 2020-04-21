a = [1,3,5,3,1]
b = []
j = 0

for i in range (len(a)):
    n = len(a)-j
    b.append(a[n-1])
    j += 1

if a == b:
    print('The massive is palindrom')
else:
    print("The massive isn't palindrom")
