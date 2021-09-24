# %%
class HM(object):
    """
    Parameters
    ----------
    dim: length of seq (i.e., len(seq))
    alpha, beta ,w : params needed to be estimated 
  
  
    Modules 
    ----------
    lik: likelihood function, return negative log likelihood (NegLL)
    fit: using non-linear Nelder-Mead simplex search algorithm to minimize NegLL summed over all trials for each subjects
    plot: 有生之年系列
    """
    
    
    from scipy.optimize import minimize
    import numpy as np
    
    def __init__(self,dim,alpha, beta, w):
        self.dim = dim
        self._init_params(alpha, beta, w)
    
    def _init_params(self,alpha, beta, w):
        import numpy as np
        self.eta = np.zeros(self.dim+1,dtype='float')    
        self.expProb = np.zeros(self.dim,dtype='float')
        self.v = np.array([0,0.75])
        self.eta[0] = 1
        self.w = w
        self.beta =beta
        self.alpha = alpha

    def lik(self,resp,seq, ro):
        """
        1. softmax function:
            p = e ** (beta*v) / ∑ e ** (beta*v)
                = 1 / (1 + e ** (beta* (v(cs-)-v(cs+)))
                = 1 / (1 + e ** (-beta * v))  # v(CS-) equals 0     
        2. update predict reward:
            v += α * η * PE
        3. calculate prediction error:
            PE = ro - v
        4. update eta: 
            η = w * |PE| + (1-w) * η
        5. NegLL
            -∑ y * log (y_hat)
        """
        import numpy as np

        for t in range(len(seq)):

            p = np.exp(self.beta*self.v) / np.sum(np.exp(self.beta*self.v))

            self.expProb[t] = p[seq[t]]

            PE = ro[t]-self.v[seq[t]]


            self.v[seq[t]] += self.alpha * PE * self.eta[t]

            self.eta[t+1] = self.w * np.abs(PE) + (1-self.w) * self.eta[t]

        _,*self.eta = self.eta
        self.eta = np.array(self.eta)
        NegLL = -np.sum(resp * np.log(self.expProb)); # 
        return NegLL


    def fit(self,resp,seq, ro):
        from scipy.optimize import minimize
        import numpy as np
        xfit = []
        LL = []
        BIC = []
        nsubj= np.shape(resp)[0]
        # loop all subject
        for ns in range(nsubj):
            def fmin(params):
                x,y,z = params
                return HM(self.dim,x,y,z).lik(resp[ns,:],seq,ro)
            x0 = np.array([0.5,4,0.5])
            bnds = ((0,1),(0,14),(0,1))
            res = minimize(fmin, x0,method = 'Nelder-Mead',bounds=bnds)

            BIC.append(len(x0)*np.log(len(resp[ns,:]))+2*res['fun'])
            LL.append(-res['fun'])
            xfit.append(res['x'])       
        xfit=np.array(xfit)
        return xfit,np.array(BIC),np.array(LL)
        
#    def plot(self):
        """
        plot everything...
        to be continued...
        """
    
if __name__ == "__main__":
    from scipy.optimize import minimize
    import numpy as np