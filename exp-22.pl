% facts
bird(sparrow).
bird(pigeon).
bird(ostrich).
bird(penguin).

% birds that can fly
can_fly(sparrow).
can_fly(pigeon).

% rule: bird can fly
fly(Bird) :-
    can_fly(Bird).

% rule: bird cannot fly
cannot_fly(Bird) :-
    bird(Bird),
    \+ can_fly(Bird).
