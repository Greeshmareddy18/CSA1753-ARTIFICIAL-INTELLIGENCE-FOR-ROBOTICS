% hanoi(NumberOfDisks, Source, Auxiliary, Destination)

hanoi(1, Source, _, Destination) :-
    write('Move disk from '), write(Source),
    write(' to '), write(Destination), nl.

hanoi(N, Source, Auxiliary, Destination) :-
    N > 1,
    M is N - 1,
    hanoi(M, Source, Destination, Auxiliary),
    write('Move disk from '), write(Source),
    write(' to '), write(Destination), nl,
    hanoi(M, Auxiliary, Source, Destination).
