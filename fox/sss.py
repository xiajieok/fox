str = "Lorem ipsum dolor sit amet"
l1 = {}
for i in str.split():
    # print(i)
    for j in i:
        l1[j] = i.count(j)
m = max(l1.values())
for k,v in l1.items():
    if v ==  m:
        print(k)

