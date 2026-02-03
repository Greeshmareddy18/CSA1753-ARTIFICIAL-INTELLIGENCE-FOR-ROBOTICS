parent(john, mary).
parent(john, tom).
parent(mary, ann).

male(john).
female(mary).
female(ann).

father(X, Y) :- male(X), parent(X, Y).
mother(X, Y) :- female(X), parent(X, Y).
