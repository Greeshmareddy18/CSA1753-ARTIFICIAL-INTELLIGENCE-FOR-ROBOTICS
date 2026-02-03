% state(MonkeyPos, BoxPos, OnBox, HasBanana)

move(state(middle, middle, onbox, no),
     state(middle, middle, onbox, yes)).

solve(State) :-
    move(State, NewState),
    write(NewState).
