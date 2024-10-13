% Facts for family relations
male(john).      % John is a male
male(bob).       % Bob is a male
female(mary).    % Mary is a female
female(lisa).    % Lisa is a female

% Parent-child relationships
parent(john, bob).  % John is a parent of Bob
parent(mary, bob).  % Mary is a parent of Bob
parent(john, lisa). % John is a parent of Lisa

% Rules for defining family relationships

% X is the father of Y if X is male and X is a parent of Y
father(X, Y) :- male(X), parent(X, Y).

% X is the mother of Y if X is female and X is a parent of Y
mother(X, Y) :- female(X), parent(X, Y).

% X is the brother of Y if X is male and both share the same parent
brother(X, Y) :- male(X), parent(Z, X), parent(Z, Y), X \= Y.

% X is the sister of Y if X is female and both share the same parent
sister(X, Y) :- female(X), parent(Z, X), parent(Z, Y), X \= Y.
