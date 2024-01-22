year = int(input('Введите год:'))
if year%4 == 0 and year%100>0:
    print("да")
else:
    print("нет")
    
# C:\Users\Alina\Desktop\Python_314\3. Python\Репозиторий\Lapik\2023.11.23>python 3.py
# Введите год:2004
# да

# C:\Users\Alina\Desktop\Python_314\3. Python\Репозиторий\Lapik\2023.11.23>python 3.py
# Введите год:1999
# нет