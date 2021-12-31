function newPop = applyMutation(pop, prob, ranges)
newPop = [];
sizeRange = ranges(:,2)-ranges(:,1);
for i = 1:length(pop)
    if(rand(1) < prob)
        lowerBound = pop(i)-(0.05*sizeRange');
        newElement = [];
        for j = 1:max(size(sizeRange))
            newElement = [newElement lowerBound(j)+(rand(1)*0.1*sizeRange(j))];
        end
        newPop = [
                newPop;
                newElement
        ];
    else
        newPop = [
            newPop;
            pop(i,:);
        ];
    end
end