a = int(input('первое число:'))
b = int(input('второе число:'))

if a%b==0:
    print(f"{a} делится на {b} нацело", f"частное:{a//b}", sep='\n')
else:
    print(f"{a} не делится на {b} нацело", f"неполное частное: {a//b}",f"остаток: {a%b}", sep='\n')
    
# C:\Users\Alina\Desktop\Python_314\3. Python\Репозиторий\Lapik\2023.11.23>python 2.py
# первое число:21
# второе число:7
# 21 делится на 7 нацело
# частное:3

# C:\Users\Alina\Desktop\Python_314\3. Python\Репозиторий\Lapik\2023.11.23>python 2.py
# первое число:10
# второе число:3
# 10 не делится на 3 нацело
# неполное частное: 3
# остаток: 1