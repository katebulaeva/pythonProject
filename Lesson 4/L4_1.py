from sys import argv
'''для расчета заработной платы" \
"введите выработку в часах " \
"потом введите ставку в час, " \
"потом введите размер бонуса'''

name, hours, rate, bonus = argv
zp = float(hours) * int(rate) + int(bonus)
print(zp)
