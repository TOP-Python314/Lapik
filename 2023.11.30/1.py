lst = []
while x := int(input()) %7 == 0:
    lst.append(x)
    lst.reverse()
    
print(lst)
# 7
# 21
# 14
# 70
# 100
# [True, True, True, True] 

#я измучилась пытаться вывести числа, не понимаю почему выводятся булевые значения 