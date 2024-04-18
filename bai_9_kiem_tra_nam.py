month,year=map(int,input("nhập tháng và năm: "))
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print("ngày của tháng {} là: 31".format(month))
elif month ==2 or month==4 or month==9 or month==11:
    print("ngày của tháng {} là: 30".format(month))
if year%400==0 or (year%4==0 and year %100!=0):
    print("{} năm nhuận".format(year))
else:
    print("{} không là năm nhuận".format(year))