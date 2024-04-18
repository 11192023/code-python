# hàm main để chạy chương trình bằng python
if __name__=="__main__":
    n=(input("nhập n: "))
    do_dai=len(n)
    tmp=n
    n=int(n)
    result=0
    for i in range(do_dai):
        print(tmp[i])
        result=result*8+int(tmp[i])
    print(result)
    