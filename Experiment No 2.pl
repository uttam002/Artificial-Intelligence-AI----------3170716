% The state is represented as [X, Y], where:
% X is the amount of water in the 4-gallon jug
% Y is the amount of water in the 3-gallon jug

% Fill the 4-gallon jug completely
move([_, Y], [4, Y]) :- Y =< 3.

% Fill the 3-gallon jug completely
move([X, _], [X, 3]) :- X =< 4.

% Empty the 4-gallon jug
move([X, Y], [0, Y]) :- X > 0.

% Empty the 3-gallon jug
move([X, Y], [X, 0]) :- Y > 0.

% Pour water from 3-gallon jug to 4-gallon jug
% If sum of both jugs exceeds 4 gallons, fill 4-gallon jug and leave rest in 3-gallon
move([X, Y], [4, Y1]) :- X + Y >= 4, Y1 is Y - (4 - X).

% Pour water from 4-gallon jug to 3-gallon jug
% If sum of both jugs exceeds 3 gallons, fill 3-gallon jug and leave rest in 4-gallon
move([X, Y], [X1, 3]) :- X + Y >= 3, X1 is X - (3 - Y).

% Pour all water from 4-gallon jug into 3-gallon jug
move([X, Y], [0, X + Y]) :- X + Y =< 3.

% Pour all water from 3-gallon jug into 4-gallon jug
move([X, Y], [X + Y, 0]) :- X + Y =< 4.
