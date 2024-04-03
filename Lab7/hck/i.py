d = {}
for _ in range(int(input())):
    name = input()
    score = float(input())
    if d.get(score) == None:
        d[score] = [name]
    else:
        d[score].append(name)


d = sorted(d.items(),-1)
d = d[::-1]
for i in sorted(d[1][1]):
    print(i)
