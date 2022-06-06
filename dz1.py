from math import factorial


def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


# №1
# Из колоды в 52 карты извлекаются случайным образом 4 карты.
# a) Найти вероятность того, что все карты – крести.
result_1a = (13 / 52) * (12 / 51) * (11 / 50) * (10 / 49)
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.
# 1 туз
C_4_1 = combinations(4, 1)
C_48_3 = combinations(48, 3)
C_1 = C_4_1 * C_48_3
# 2 туза
C_4_2 = combinations(4, 2)
C_48_2 = combinations(48, 2)
C_2 = C_4_2 * C_48_2
# 3 туза
C_4_3 = combinations(4, 3)
C_48_1 = combinations(48, 1)
C_3 = C_4_3 * C_48_1
# 4 туза
C_4 = 1
C = C_1 + C_2 + C_3 + C_4
# все исходы
C_all = combinations(52, 4)
result_1b = C / C_all

# №2
# На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9. Код содержит три
# цифры, которые нужно нажать одновременно. Какова вероятность того, что человек, не знающий код, откроет дверь
# с первой попытки?
C_all = combinations(10, 3)
result_2 = 1 / C_all

# №3
# В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 детали. Какова вероятность
# того, что все извлеченные детали окрашены?
result_3 = (9 / 15) * (8 / 14) * (7 / 13)

# №4
# В лотерее 100 билетов. Из них 2 выигрышных. Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?
result_4 = (2 / 100) * (1 / 99)
