from math import*
#viết hàm phân tích thừa số nguyên tố theo mẫu
def ana_iprime(n):
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            dem=0
            while n%i==0:
                dem+=1
                n//=i
            print("{0}^")