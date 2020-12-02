pasta_1 = int(input())
pasta_2 = int(input())
pasta_3 = int(input())

juice_1 = int(input())
juice_2 = int(input())

cheapest_pasta = min(pasta_1, pasta_2, pasta_3)
cheapest_juice = min(juice_1, juice_2)

result = (cheapest_juice + cheapest_pasta) * 1.1
print("%.1f" % result)
