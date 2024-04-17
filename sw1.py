 import heapq

def calculate_relevance(a, f):
    return sum(a[i] * f[i] for i in range(len(a)))

n = int(input())
a = list(map(int, input().split()))
d = int(input())
features = []
for _ in range(d):
    f = list(map(int, input().split()))
    features.append(f)

q = int(input())
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        k = query[1]
        objects = []
        for i in range(d):
            relevance = calculate_relevance(a, features[i])
            objects.append((-relevance, i+1))
        heapq.heapify(objects)
        top_k = heapq.nsmallest(k, objects)
        print(' '.join(str(index) for relevance, index in top_k))
    else:
        _, i, j, v = query
        features[i-1][j-1] = v
