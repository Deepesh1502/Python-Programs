n=int(input("Enter a number: "))
s=0
t=n
while t>0:
   r=t%10
   s=(s*10)+r
   t=t//10
   
if n==s:
   print (n, "is pallindrome")
else:
   print (n, "is not pallindrome")
