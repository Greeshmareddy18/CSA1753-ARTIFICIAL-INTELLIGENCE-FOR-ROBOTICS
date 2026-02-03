% pattern matching facts
likes(john, apple).
likes(mary, banana).
likes(john, banana).

% rule for matching
match(Person, Fruit) :-
    likes(Person, Fruit).
