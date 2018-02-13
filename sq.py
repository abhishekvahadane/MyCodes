def fisr(x):
  a=0
  b=x
  r=a
  inc=0.00
  e=0.000001
  while(1):
    r=(a+b)/2
    if abs(r*r-x)<e:
      break
    elif (r*r<x):
      a=r
    else:
      b=r
  print('square root is %f'%r)
  return r
  
print("computing the square root")
ans=fisr(100)
