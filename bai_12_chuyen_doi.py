# hàm main để chạy chương trình bằng python
kt=input("nhập chuỗi: ")
do_dai=len(kt)
do_dai_spam=len("spam")
end=""
start=0
for i in range(do_dai):
    pos=kt[start:].find("spam")
    if pos!=-1:
        for j in range(i,pos):
            end+=kt[j]
        
    
    


