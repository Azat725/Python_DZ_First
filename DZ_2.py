salary = int(input('Введите свою зарплату: '))
utilities = int(input('Введите плату за коммунальные услуги: '))
credit = int(input('Введите платеж за кредит(ипотеку) в банке: '))

remains = salary - credit - utilities
print('На вашем счету останеться: ', remains, 'рублей')