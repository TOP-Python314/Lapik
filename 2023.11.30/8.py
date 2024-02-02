n = int(input())

a = 0 
b = 1 
i = 0 
while i < n: 
        print(a, end=" ") 
        c = a + b 
        a = b 
        b = c 
        i += 1 

# C:\Users\Alina\Desktop\Python_314\3. Python\Репозиторий\Lapik\2023.11.30>python 8.py
# 7
# 0 1 1 2 3 5 8