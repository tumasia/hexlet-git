name = input('Как тебя зовут? ')
message = 'Привет, ' + name + '.'
print(message)
response = input('В каком году ты родился?')
year = int(response)
age = 2022 - year
print('Тебе ' + str(age) + ' лет.')
