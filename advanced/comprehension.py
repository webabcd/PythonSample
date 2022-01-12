# comprehension 推导式

a = [1, 2, 3, 4, 5]
b = {1, 2, 3, 4, 5}
c = {"k1":1, "k2":2, "k3":3, "k4":4, "k5":5}

d = [x for x in a if x % 2 == 0]
e = {x for x in b if x % 2 == 0}
f = {k:v for k,v in c.items() if v % 2 == 0}
print(d) # [2, 4]
print(e) # {2, 4}
print(f) # {'k2': 2, 'k4': 4}

g = [(x,y) for x in range(2) for y in range(3)] 
print(g) # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]

h = {f"k{x}_{y}":f"v{x}_{y}" for x in range(2) for y in range(3)}
print(h) # {'k0_0': 'v0_0', 'k0_1': 'v0_1', 'k0_2': 'v0_2', 'k1_0': 'v1_0', 'k1_1': 'v1_1', 'k1_2': 'v1_2'}

i = [(x,y) for x in range(2) if x % 2 == 0 for y in range(3) if y % 2 == 0] 
print(i) # [(0, 0), (0, 2)]



j = [[0 for col in range(2)] for row in range(3)]
print(j) # [[0, 0], [0, 0], [0, 0]]

def max(a, b):
    if a > b:
        return a
    else:
        return b
k = [max(x,y) for x in range(2) for y in range(3)] 
print(k) # [0, 1, 2, 1, 1, 2]
