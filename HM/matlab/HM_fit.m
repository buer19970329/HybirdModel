function [Xfit, LL, BIC] = HM_fit(a, seq,ro)


matrix = size(a);
nsubj =matrix(1);

for ns = 1:nsubj
    obFunc = @(x) HM_lik(a(ns,:),seq, ro, x(1), x(2), x(3));
    
    X0 = [0.5,4,0.5];  % x 的初始点    
    % plot the objective function at each iteration
    options = optimset('PlotFcns',@optimplotfval);    
    [Xfit(ns,:), NegLL(ns,:)] = fminsearch(obFunc, X0, options);




    LL(ns,:) = -NegLL(ns,:);
    BIC(ns,:) = length(X0) * log(length(a)) + 2*NegLL(ns,:);
end

LL = LL
BIC = BIC
