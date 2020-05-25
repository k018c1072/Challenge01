# amount_of_money -> 金額
# 省略 money

money = int(input('金額 > '))
print('10000円札', money // 10000)
money -= (money // 10000) * 10000
print('5000円札', money // 5000)
money -= (money // 5000) * 5000
print('1000円札', money // 1000)
