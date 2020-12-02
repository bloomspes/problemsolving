a, b, c, d, e = int(input())

get_min_pasta = min(a, b, c)
get_min_juice = min(d, e)

result = (get_min_pasta + get_min_juice) * 1.1
print("%.1f" % result)
