a,b=map(float,input().split())
if (a<=b and a%5!=0) or a>b:
    print("%.2f"%b)
else:
    c=b-a-0.5
    print("%.2f"%c)
