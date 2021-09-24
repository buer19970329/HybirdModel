# %%
def HM_lik(response, data,ro,alpha,beta,w):
    import numpy as np

    eta = np.zeros(np.shape(data)[0]+1,dtype='float')    
    expProb = np.zeros_like(data,dtype='float')
    valueV = np.zeros_like(data,dtype='float')
    v = np.array([0,0.75])
    eta[0] = 1
    
    
    p1=np.zeros_like(data,dtype='float')
    p2=np.zeros_like(data,dtype='float')

    for t in range(len(data)):
        
        p = np.exp(beta*v) / np.sum(np.exp(beta*v))
        
        expProb[t] = p[data[t]]
        p1[t] = p[0]
        p2[t] = p[1]
        
        PE = ro[t]-v[data[t]]
        
        
        v[data[t]] = v[data[t]] + alpha * PE * eta[t]
        
        eta[t+1] = w * np.abs(PE) + (1-w) * eta[t]
        
        valueV[t] = v[data[t]]
        
    _,*eta = eta
    NegLL = -np.sum(response * np.log(expProb));
    eta = np.array(eta)
    return NegLL