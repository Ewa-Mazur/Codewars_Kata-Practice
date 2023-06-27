find_uniq= [ 0, 0, 0.55, 0, 0 ]
#print(find_uniq)

x = list(set(find_uniq))


if find_uniq.count(x[0]) < find_uniq.count(x[1]):
    print('unique number isss', x[0])
else:
    print('unique number isss', x[1])


