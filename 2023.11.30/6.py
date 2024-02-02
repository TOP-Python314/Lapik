number = str(input('номер билета: '))
ticket = [int(x) for x in number]
middle = len(ticket) // 2

if sum(ticket[0:middle]) == sum(ticket[middle:]):
    print('да')
else:
    print('нет')
   
# C:\Users\Alina\Desktop\Python_314\3. Python\Репозиторий\Lapik\2023.11.30>python 6.py
# номер билета: 183534
# да

# C:\Users\Alina\Desktop\Python_314\3. Python\Репозиторий\Lapik\2023.11.30>python 6.py
# номер билета: 678935
# нет