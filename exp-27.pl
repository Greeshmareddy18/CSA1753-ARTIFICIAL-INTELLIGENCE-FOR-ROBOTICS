edge(a,b).
edge(a,c).
edge(b,goal).
edge(c,goal).

h(b,1).
h(c,2).

best(a,goal) :- edge(a,b).
