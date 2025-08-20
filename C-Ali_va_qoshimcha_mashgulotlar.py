n=int(input())
k=int(input())
d=input().split()
b=int(input())
holidays=set(input().split()) if b>0 else set()
days=["Dushanba","Seshanba","Chorshanba","Payshanba","Juma","Shanba","Yakshanba"]
months=[31,28,31,30,31,30,31,31,30,31,30,31]
s=0
day=0
for mi,m in enumerate(months,1):
  cnt=0
  for di in range(1,m+1):
    wd=days[day%7]
    if wd in d:
      date=f"{di:02d}.{mi:02d}"
      if date not in holidays:
        cnt+=1
    day+=1
  if cnt>0:
    s+=n
    per=n/cnt
    for di in range(1,m+1):
      wd=days[(day-m+di-1)%7]
      if wd in d:
        date=f"{di:02d}.{mi:02d}"
        if date in holidays:
          s-=per
print(int(s))
