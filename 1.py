name,surname,birthDate = str(input('Введите имя ')),str(input('Введите фамилию ')),int(input('Введите год рождения '))
print(name,surname,birthDate)
name,surname = surname,name
print(name,surname,birthDate+60)