def get_xalpha(x, alpha, k):
    from pars_data import data
    return data[alpha][k-1]
    pass

n = (105, 140, 125, 160)
m = (60, 69, 63, 105)
alpha =	0.05

k = len(n) - 1

p = sum(m) / sum(n)

w = list(map(lambda m, n: m / n, m, n))

x = (1 / (p * (1 - p)) * sum([n[i] * (w[i] - p) ** 2 for i in range(len(n))]))
xalpha = get_xalpha(x, alpha, k)

print(f'Так как {x} {[">", "<"][x < xalpha]} {xalpha}, то на уровне alpha = {alpha} {["гипотеза H0 принимается", "Гипотеза H0 отвергается"][x > xalpha]}')