% planet(Name, Type, DistanceFromSun_million_km)
planet(mercury, terrestrial, 57).
planet(venus, terrestrial, 108).
planet(earth, terrestrial, 150).
planet(mars, terrestrial, 228).
planet(jupiter, gas_giant, 778).

% rule: check if a planet is terrestrial
terrestrial_planet(Planet) :-
    planet(Planet, terrestrial, _).
