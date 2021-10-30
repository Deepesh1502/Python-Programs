num=int(input("Enter a number: "))
s=0
t=num
while t>0:
   r=t%10
   s=s+r**3
   t=t//10
if s==num:
   print (num, "Number is Armstrong")
else:
   print (num, "Number is not Armstrong")
