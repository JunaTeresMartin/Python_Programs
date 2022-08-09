def intreverse(n):
  l=0
  m=1
  while(n>0):
    r=n%10
    n=n//10
    l=(l*m)+r
    m=10
  print(l)
intreverse(n=int(input()))
