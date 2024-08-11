
n = int(input("Enter number: "))
even_sum = 0

for i in range(1, n+1):
    if i % 2 == 0:
        print(i)
        even_sum += i
print(even_sum)        