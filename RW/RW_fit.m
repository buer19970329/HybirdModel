function [Xfit, LL, BIC] = RW_fit(a, ro)


matrix = size(a);
nsubj =matrix(1);

for ns = 1:nsubj
    obFunc = @(x) RW_lik(a(ns,:), ro, x(1), x(2));

    X0 = [rand exprnd(1)];  % x 的初始点
    LB = [0 0];             % lower boundary
    UB = [1 inf];           % upper boundary
    [Xfit(ns,:), NegLL(ns,:)] = fmincon(obFunc, X0, [], [], [], [], LB, UB);




    LL(ns,:) = -NegLL(ns,:);
    BIC(ns,:) = length(X0) * log(length(a)) + 2*NegLL(ns,:);
end

LL = LLfmincon
BIC = BIC
Xfit = Xfit
NegLL = NegLL
