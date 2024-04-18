a,b,c=map(int,input("nhập a,b,c: "))
if a>0 and b>0 and c>0 and a+b>c and b+c>a and a+c>b:
    cv=a+b+c
    print(cv)
else:
    print("tam giác không hợp lệ")