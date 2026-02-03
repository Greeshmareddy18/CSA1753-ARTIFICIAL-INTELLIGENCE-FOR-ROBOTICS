% symptoms
symptom(fever).
symptom(cough).
symptom(headache).

% disease rules
disease(flu) :-
    symptom(fever),
    symptom(cough).

disease(migraine) :-
    symptom(headache).

% diagnosis rule
diagnose(Disease) :-
    disease(Disease).
