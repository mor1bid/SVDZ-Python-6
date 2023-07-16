def real(date):
    date = date.split('.')
    if int(date[2]) > 9999 or int(date[2]) < 1:
        res = False
    else:
        res = True
    return res

def super(date):
    _supereal(date)

def _supereal(date):
    res = 'невисокосный'
    date = date.split('.')
    if int(date[2]) % 4 == 0 or int(date[2]) % 100 == 0 and int(date[2]) % 400 == 0:
        res = 'високосный'
    print("Данный год -", res)

date = input("1. Здравствуйте. Введите желаемую дату в формате день.месяц.год\n: ")
super(date)
print("Данная дата допустима?", real(date))