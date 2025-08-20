n=int(input())
s=0
for i in range(n):
  l=input().strip()
  a=l.split(':',1)[1].strip()
  b=a.split(';',1)
  p=int(b[0])
  c=b[1].strip()
  if c.endswith('x'):
    c=c[:-1]
  c=int(c)
  s+=p*c
print(s)
