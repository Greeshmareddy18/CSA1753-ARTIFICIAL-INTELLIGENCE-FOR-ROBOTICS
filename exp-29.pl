% facts
fact(a).
fact(b).

% rule
fact(c) :- fact(a), fact(b).
fact(d) :- fact(c).
