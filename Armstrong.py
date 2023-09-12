n=int(input('Enter your number'))
order=len(n)
sum=0,temp=n
while temp >0:
  digit = temp%10
  sum+=digit**order
  temp=temp//10
if n == sum:
  print('Number is Armstrong')
else:
  print("Print number is not armstrong")
