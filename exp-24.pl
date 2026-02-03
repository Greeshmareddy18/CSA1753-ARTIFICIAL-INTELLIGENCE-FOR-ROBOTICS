% diet(Disease, SuggestedDiet)
diet(diabetes, low_sugar).
diet(bp, low_salt).
diet(obesity, low_fat).
diet(anemia, iron_rich).

% rule to suggest diet
suggest_diet(Disease, Diet) :-
    diet(Disease, Diet).
