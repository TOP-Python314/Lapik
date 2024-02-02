t = input('Текст телеграммы:')
lst = list(t.split())
price = sum(len(i) for i in lst)*0.30
print(f'{price} руб.')

# C:\Users\Alina\Desktop\Python_314\3. Python\Репозиторий\Lapik\2023.11.30>python 5.py
# Текст телеграммы:грузите апельсины бочках братья карамазовы
# 11.4 руб.