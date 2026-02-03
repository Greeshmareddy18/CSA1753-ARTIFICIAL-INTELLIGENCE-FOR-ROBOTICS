% facts
fruit_color(apple, red).
fruit_color(apple, green).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(grape, green).

% rule
color_of_fruit(Fruit, Color) :-
    fruit_color(Fruit, Color).
