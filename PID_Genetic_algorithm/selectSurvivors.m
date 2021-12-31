function survivors = selectSurvivors(pop, best2)
pop = [
    best2;
    pop;
];
errors = [];
for i = 1:size(pop,1)
    [ISE,t_r,t_s,M_p] = perfFCN(pop(i,:)');
    errors = [
        errors;
        ISE,t_r,t_s,M_p;
    ];
end

fitness = getFitness(errors);

% remove worst 2 in place of the best 2
[~, idx] = min(fitness, [], 1);
pop(idx,:) = [];
fitness(idx,:) = [];
[~, idx] = min(fitness, [], 1);
pop(idx,:) = [];
fitness(idx,:) = [];
survivors = pop;
