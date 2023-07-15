from mod_DMY import real, super

# 7
mydate = input("7. Здравствуйте. Введите желаемую дату в формате день.месяц.год\n: ")
print("Данный год -", super(mydate))
print("Данная дата допустима?", real(mydate))