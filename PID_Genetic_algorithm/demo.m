popSize = 50;
numGenerations = 150;
mutationProbability = 0.25;
crossOverProbability = 0.6;
ranges = [
    2 18;
    1.05 9.42;
    0.26 2.37;
];
%% part c
[solution0, ~, ~, ~, ~, solutionFitness0] = GA(popSize,numGenerations, mutationProbability, crossOverProbability, ranges);

%% part d
plot(1:numGenerations, solutionFitness0);
title('Max Fitness of solutions vs generation')
xlabel('Generation')
ylabel('Fitness')

%% part e setup
numGenerations = 50;
[solutionE1, ~, ~, ~, ~, solutionFitnessE1] = GA(popSize,numGenerations, mutationProbability, crossOverProbability, ranges);
numGenerations = 300;
[solutionE2, ~, ~, ~, ~, solutionFitnessE2] = GA(popSize,numGenerations, mutationProbability, crossOverProbability, ranges);
%% Part e plotting
plot(1:300, solutionFitnessE2);
hold on;
plot(1:150, solutionFitness0);
plot(1:50, solutionFitnessE1);
title('Max Fitness of solutions vs generation')
xlabel('Generation')
ylabel('Fitness')
legend('300 generations','150 generations','50 generations')
hold off;

%% part f setup
numGenerations = 150;
popSize = 20;
[solutionF1, ~, ~, ~, ~, solutionFitnessF1] = GA(popSize,numGenerations, mutationProbability, crossOverProbability, ranges);
popSize = 100;
[solutionF2, ~, ~, ~, ~, solutionFitnessF2] = GA(popSize,numGenerations, mutationProbability, crossOverProbability, ranges);
%% Part f plotting
plot(1:numGenerations, solutionFitnessF1);
hold on;
plot(1:numGenerations, solutionFitness0);
plot(1:numGenerations, solutionFitnessF2);
title('Max Fitness of solutions vs generation')
xlabel('Generation')
ylabel('Fitness')
legend('20 population','50 population','100 population')
hold off;
%% part g setup
popSize = 50;
crossOverProbability = 0.2;
[solutionG1, ~, ~, ~, ~, solutionFitnessG1] = GA(popSize,numGenerations, mutationProbability, crossOverProbability, ranges);
crossOverProbability = 0.9;
[solutionG2, ~, ~, ~, ~, solutionFitnessG2] = GA(popSize,numGenerations, mutationProbability, crossOverProbability, ranges);

%% part g plotting
plot(1:numGenerations, solutionFitnessG1);
hold on;
plot(1:numGenerations, solutionFitness0);
plot(1:numGenerations, solutionFitnessG2);
title('Max Fitness of solutions vs generation')
xlabel('Generation')
ylabel('Fitness')
legend('0.2 crossover','0.6 crossover','0.9 crossover')
hold off;
%% part h setup
crossOverProbability = 0.6;
mutationProbability = 0.1;
[solutionH1, ~, ~, ~, ~, solutionFitnessH1] = GA(popSize,numGenerations, mutationProbability, crossOverProbability, ranges);
mutationProbability = 0.5;
[solutionH2, ~, ~, ~, ~, solutionFitnessH2] = GA(popSize,numGenerations, mutationProbability, crossOverProbability, ranges);

%% part h plotting
plot(1:numGenerations, solutionFitness0);
hold on;
plot(1:numGenerations, solutionFitnessH1);
plot(1:numGenerations, solutionFitnessH2);
title('Max Fitness of solutions vs generation')
xlabel('Generation')
ylabel('Fitness')
legend('0.1 mutation','0.25 mutation','0.5 mutation')
hold off;