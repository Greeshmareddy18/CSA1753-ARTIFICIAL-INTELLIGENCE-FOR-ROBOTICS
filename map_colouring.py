def safe(r, c, a, g):
    return all(a.get(n) != c for n in g[r])

def map_color(g, colors, a):
    if len(a) == len(g): return a
    r = next(x for x in g if x not in a)
    for c in colors:
        if safe(r, c, a, g):
            a[r] = c
            if map_color(g, colors, a): return a
            del a[r]

graph = {
    'A':['B','C'],
         'B':['A','C','D'],
         'C':['A','B','D'],
         'D':['B','C']
         }
colors = ['Red','Green','Blue']

print(map_color(graph, colors, {}))
