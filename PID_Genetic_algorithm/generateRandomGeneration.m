function newPop = generateRandomGeneration(num, ranges)
rng(457);
newPop = [];
sizeRange = ranges(:,2)-ranges(:,1);
rangeLowerBound = ranges(:,1);
for i = 1:num
    newElement = [];
    for j = 1:max(size(rangeLowerBound))
        newElement = [newElement rangeLowerBound(j)+(rand(1)*sizeRange(j))];
    end
    newPop = [
        newPop;
        newElement;
    ];
end