# %%

def HM_fit(data,ro):
    from scipy.optimize import minimize
    import numpy as np
    from HM_lik import HM_lik

    xfit = []
    LL = []
    BIC = []
    nsubj= np.shape(data)[0]
    # loop all subj
    for ns in range(nsubj):
        # 定义 observe funciton
        def obFunc(params):
            x,y,z = params # x,y,z分别对应3个free parameter
            return HM_lik(data[ns,:], ro, x,y,z)
        x0 = np.array([0.5,4,0.5]) # initial value
        bnds = ((0,1),(0,14),(0,1)) # boundary * 3
        res = minimize(obFunc, x0,method = 'Nelder-Mead',bounds=bnds) # Using nonlinear optimization 'Nelder-Mead' to fit model as paper used
        
        BIC.append(len(x0)*np.log(len(data[ns,:]))+2*res['fun'])
        LL.append(-res['fun'])
        xfit.append(res['x'])       
    xfit=np.array(xfit)
    return xfit,np.array(LL),np.array(BIC)
