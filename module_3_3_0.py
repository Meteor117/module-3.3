# 1.Функция с параметрами по умолчанию (работает!!!)

def print_params (a=1, b='Str', c=True):
   print (a, b, c)

print_params()
print_params(b=25)# проверка работы функции с изменением параметра 'b' = 25, функция рботает!
print_params(c=[1, 2, 3])# проверка работы функции с изменением параметра 'с'= [1, 2, 3], функция работает!

# 2. Распаковка параметров (работает!!!)
def print_params(*args,**kwargs):
    for key,value in kwargs.items():
        print(key,value)

values_list=[1, 'Str', True]
values_dict={'a':1, 'b':'Str', 'c':True}

print_params(*values_list,**values_dict)


# 3.Распаковка+отдельные параметры (работает!!!)
def print_params(a, b, c):
    print(a, b, c)

values_list_2=[54.32, 'Строка']

print_params(*values_list_2, 42)


