% Defining entities and relationships in a Semantic Net

% Entities: Defining some basic facts about animals and objects
cat(tom).        % Tom is a cat
cat(cat1).       % Cat1 is another cat
mat(mat1).       % Mat1 is a mat

% Relationships: Using predicates to link the entities
sat_on(cat1, mat1).  % Cat1 is sitting on Mat1
bird(bird1).         % Bird1 is a bird
caught(tom, bird1).  % Tom caught Bird1

% Additional facts for semantic understanding
like(cat1, cream).   % Cat1 likes cream
mammal(cat1).        % Cat1 is a mammal
has(cat1, fur).      % Cat1 has fur
animal(X) :- mammal(X).  % Mammals are animals
owns(john, tom).     % John owns Tom
is_coloured(tom, ginger). % Tom is ginger-colored
