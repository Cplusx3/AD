from math import sqrt
from parse_data import data

def get_tkp(f):
    for i in data:
        if f < i:
            return data[[i, prev][(abs(prev - f) < (abs(i - f)))]]
        prev = i
           

n1 = 100
n2 = 120
m1 = 58
m2 = 65
a =	0.02
w1 = m1 / n1
w2 = m2 / n2
p = (m1 + m2) / (n1 + n2)

t = (w1 - w2) / sqrt(p * (1 - p) * (1 / n1 + 1 / n2))
tkp = get_tkp(1 - a)

print(t)
print(f'т.к |{t}| {["<", ">"][abs(t) > tkp]} {tkp}, то {["Гипотеза H0 отвергается", "Гипотеза H0 принимается"][t < tkp]}')