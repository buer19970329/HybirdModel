# HybirdModel

Code and behavioural data for:

Esser, R., Korn, C. W., Ganzer, F., & Haaker, J. (2021). L-DOPA modulates activity in the vmPFC, nucleus accumbens, and VTA during threat extinction learning in humans. eLife, 10, e65280. https://doi.org/10.7554/eLife.65280

-----

This repository contains:

# 1. Rescorla-Wagner model (RW)
```
A basic model for Reinforcement Learning
```
* Matlab scripts: [RW_lik.m](RW/RW_lik.m) → [RW_fit.m](RW/RW_fit.m)


### Reference:
Lockwood, P. L., & Klein-Flügge, M. C. (2021). Computational modelling of social cognition and behaviour—a reinforcement learning primer. Social cognitive and affective neuroscience, 16(8), 761-771.

# 2. Rescorla-Wagner-Pearce-Hall-Hybrid model (HM)
```
The model used in (Esser et al., 2021)
```
* Matlab scripts: [HM_lik.m](HM/matlab/HM_lik.m) → [HM_fit.m](HM/matlab/HM_fit.m)
* Python scripts (highly recommended): [HM_lik.py](HM/HM_lik.py) → [HM_fit.py](HM/HM_fit.py)
* Here is a pipeline from data processing to model fitting: [pipeline.ipynb](pipeline.ipynb)


### Reference:
Esser, R., Korn, C. W., Ganzer, F., & Haaker, J. (2021). L-DOPA modulates activity in the vmPFC, nucleus accumbens, and VTA during threat extinction learning in humans. eLife, 10, e65280. https://doi.org/10.7554/eLife.65280


Have fun :)
