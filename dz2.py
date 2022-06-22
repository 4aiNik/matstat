from math import factorial
from math import e


def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


# №1
# Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8. Стрелок выстрелил 100 раз.
# Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.
p1 = 0.8
n1 = 100
k1 = 85
result1 = combinations(n1, k1) * (p1 ** k1) * ((1 - p1) ** (n1 - k1))
print(result1)
# ответ 0.048061793700746355

# 2 Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004. В жилом комплексе
# после ремонта в один день включили 5000 новых лампочек. Какова вероятность, что ни одна из них не перегорит в первый
# день? Какова вероятность, что перегорят ровно две?
n2 = 5000
m2_1 = 0
m2_2 = 2
l2 = 0.0004 * 5000
result2_1 = (l2 ** m2_1) / factorial(m2_1) * (e ** (- l2))
print(result2_1)
# ответ 0.1353352832366127
result2_2 = (l2 ** m2_2) / factorial(m2_2) * (e ** (- l2))
print(result2_2)
# ответ 0.2706705664732254

# 3 Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?
p3 = 0.5
n3 = 144
k3 = 70
result3 = combinations(n3, k3) * (p3 ** k3) * ((1 - p3) ** (n3 - k3))
print(result3)
# ответ 0.06281178035144776

# 4 В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей, из которых 9 белых.
# Из каждого ящика вытаскивают случайным образом по два мяча. Какова вероятность того, что все мячи белые?
# Какова вероятность того, что ровно два мяча белые? Какова вероятность того, что хотя бы один мяч белый?
result4_1 = combinations(7, 2) / combinations(10, 2) * combinations(9, 2) / combinations(11, 2)
print(result4_1)
# ответ 0.3054545454545455

ww_bb = combinations(7, 2) / combinations(10, 2) * combinations(2, 2) / combinations(11, 2)
bb_ww = combinations(3, 2) / combinations(10, 2) * combinations(9, 2) / combinations(11, 2)
wb_wb = (combinations(7, 1) * combinations(3, 1) / combinations(10, 2)) * \
        (combinations(9, 1) * combinations(2, 1) / combinations(11, 2))
result4_2 = ww_bb + bb_ww + wb_wb
print(result4_2)
# ответ 0.20484848484848486

all_black = combinations(3, 2) / combinations(10, 2) * combinations(2, 2) / combinations(11, 2)
result4_3 = 1 - all_black
print(result4_3)
# ответ 0.9987878787878788
