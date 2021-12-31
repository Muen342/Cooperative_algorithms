function [solution, ISE, t_r, t_s, M_p, solutionFitness] = GA(popSize,numGenerations, mutationProbability, crossOverProbability, ranges)
% first generation
population = generateRandomGeneration(popSize, ranges);
generation = 0;
% run through generations
bestSolutionFitness = [];
while(generation < numGenerations)
    errors = [];
    for i = 1:size(population,1)
        [ISE,t_r,t_s,M_p] = perfFCN(population(i,:)');
        errors = [
            errors;
            ISE,t_r,t_s,M_p;
        ];
    end
    fitness = getFitness(errors);
    bestSolutionFitness = [bestSolutionFitness max(fitness)];
    parents = selectParents(population,popSize);
    % best 2 selected as parents and inserted to final population as well
    best2 = parents(1:2,:);
    population = applyCrossover(parents, crossOverProbability);
    population = applyMutation(population, mutationProbability,ranges);

    % insert 2 best for elitism again and re-evaluate if they are best, if
    % they are include them again automatically here
    population = selectSurvivors(population, best2);
    generation = generation + 1;
end
errors = [];
for i = 1:size(population,1)
    [ISE,t_r,t_s,M_p] = perfFCN(population(i,:)');
    errors = [
        errors;
        ISE,t_r,t_s,M_p;
    ];
end
fitness = getFitness(errors);
[~, idx] = max(fitness, [], 1);
solution = population(idx,:);
ISE = errors(idx,1);
t_r = errors(idx,2);
t_s = errors(idx,3);
M_p = errors(idx,4);
solutionFitness = bestSolutionFitness;

