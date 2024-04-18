# hàm main để chạy chương trình bằng python
hex_to_decimal = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                  'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

hex_digit = 'FF'  
a=0
for i in range (len(hex_digit)):
    a =a*16+ hex_to_decimal[hex_digit[i].upper()]
print(a)

