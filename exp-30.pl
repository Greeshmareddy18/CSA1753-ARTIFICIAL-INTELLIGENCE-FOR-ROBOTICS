% facts
parent(john, mary).
parent(mary, ann).

% rules
ancestor(X, Y) :-
    parent(X, Y).

ancestor(X, Y) :-
    parent(X, Z),
    ancestor(Z, Y).
