print("trời hôm nay có mưa không")
s=input("the user: ")
s=s.lower()
print(s)
if s=="yes":
    print("trời có gió không")
    s1=input("the user: ")
    s1=s1.lower()
    print(s1)
    if s1=="yes":
        print("trời quá gió để mang ô")
    else:
        print("take an unbrella")
else:
    print("enjoy your day")