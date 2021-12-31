function parents = selectParents(pop, popSize)
totalElements = popSize-2;
%% set probabilities to get selected
errors = [];
for i = 1:size(pop,1)
    [ISE,t_r,t_s,M_p] = perfFCN(pop(i,:)');
    errors = [
        errors;
        ISE,t_r,t_s,M_p;
    ];
end

%% remove nans as they are unnecessary and should have 0 weight
fitness = getFitness(errors);
nans = isnan(fitness);
fitness(nans,:) = [];
pop (nans,:) = [];

%% choose the top 2 for elitism
parents = [];
[~, idx] = max(fitness, [], 1);
parents(1,:) = pop(idx,:);
fitness(idx,:) = [];
pop(idx,:) = [];

[~, idx] = max(fitness, [], 1);
parents(2,:) = pop(idx,:);
fitness(idx,:) = [];
pop(idx,:) = [];

%% use baker stochastic universal sampling
total = sum(fitness);
prob = fitness/total;

displacement = rand(1)/totalElements;
step = 1/totalElements;

% make the probability vector show the cumulative probability
current = 0;
for i = 1:length(prob)
    prob(i) = prob(i) + current;
    current = prob(i);
end

for i = 1:totalElements
    point = mod(i*step + displacement,1);
    for j = 1:length(prob)
        if(j ~= length(prob))
            if(prob(j+1) >= point)
                parents = [
                    parents;
                    pop(j,:);
                ];
                break;
            end
        else
            if(prob(1) >= point)
                parents = [
                    parents;
                    pop(length(prob),:);
                ];
                break
            end
        end
    end
end