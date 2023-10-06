def KT_Fibonacci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return KT_Fibonacci(n-1) + KT_Fibonacci(n-2)

dayso=[2,3,4,5,6,7,8,9,15]
a = ""
for i in dayso:
   
    a = a + str(KT_Fibonacci(i)) + ","
print(a)




