% student(StudentName, Subject, SubjectCode)
student(john, math, m101).

% teacher(TeacherName, Subject, SubjectCode)
teacher(smith, math, m101).

% rule: teacher teaches student if subject and code match
teaches(Teacher, Student) :-
    teacher(Teacher, Subject, Code),
    student(Student, Subject, Code).
