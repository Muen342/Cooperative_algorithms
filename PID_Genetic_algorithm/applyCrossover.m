function newPop = applyCrossover(parents, prob)
newPop = [];
alpha = 0.6;
% randomly shuffle
parents = parents(randperm(size(parents, 1)), :);

% if odd, first parent is automatically chosen as child
if(mod(size(parents,1),2) == 1)
    newPop = parents(1,:);
    parents(1,:) = [];
end

for i = 1:size(parents,1)/2
    % apply crossover
    if(rand(1) < prob)
        child1 = (parents(2*i-1,:)*alpha) + (parents(2*i,:)*(1-alpha));
        child2 = (parents(2*i-1,:)*(1-alpha)) + (parents(2*i,:)*(alpha));
        newPop = [
            newPop;
            child1;
            child2;
        ];
    % pass down parents instead
    else
        newPop = [
            newPop;
            parents(2*i-1,:);
            parents(2*i,:)
        ];
    end
end