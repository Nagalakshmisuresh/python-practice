n=int(input("Enter a number"))
sum=0
temp=n
while(n!=0):
    rem=n%10
    fact=1
    while(rem!=0):
        fact=fact*rem
        rem=-1
    sum=sum+fact
    n=n//10
if temp==sum:
    print("strong")
else:
    print("not strong")
        