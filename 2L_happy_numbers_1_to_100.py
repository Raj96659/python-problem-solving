#  Write a Python program to print all happy numbers between 1 and 100

for num in range(2,101):
    temp=num
    seen = set()
    while temp!=1 and temp not in seen:
        seen.add(temp)
        sum = 0
        for i in str(temp):
            sum = sum + int(i)**2
        #print(sum)
        temp = sum

    if temp == 1:
        print(num,'is happy')
