function fitness = getFitness(errors)
%% increase the scale so easier to use
fitness = 100000./prod(errors,2);