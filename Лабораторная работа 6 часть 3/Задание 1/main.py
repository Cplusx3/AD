from math import sqrt
from parse_data import data

def get_critical_area(x, y, a, H):
    if 'H1' == H:
        t = 1 - 2 * a
    else:
        t = 1 - a
    return t
    
def get_tkp(f):
    for i in data:
        if f < i:
            return data[[i, prev][(abs(prev - f) < (abs(i - f)))]]
        prev = i
           
       
σx2 = 100
σy2 = 74
n1 = 50
n2 = 70
x = 85
y = 78
a = 0.05
h = 'H1'

t = (x - y)/sqrt(σx2 / n1 + σy2 / n2)
tkp = get_tkp(get_critical_area(x, y, a, h))
print(f'т.к {t} {["<", ">"][t > tkp]} {tkp}, то {["Гипотеза H0 отвергается", "Гипотеза H0 принимается"][t < tkp]}')