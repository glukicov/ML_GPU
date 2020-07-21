'''
Author: Gleb Lukicov

Auxiliary functions 
'''
import numpy as np 
from scipy import stats

### Stat functions

def ci(pred, test, cl=0.95):
    '''
    t-score CI 
    '''
    print("Calculating a",int(cl*100),"% CI...")
    squared_errors = (pred - test) ** 2
    DoF = len(squared_errors) - 1
    sample_mean = squared_errors.mean()
    sample_standard_error = stats.sem(squared_errors)
    return np.sqrt(  stats.t.interval( cl, DoF, loc=sample_mean, scale= sample_standard_error )  )

def sigma(pred, test, cl=0.95):
    '''
    Standard score (z-score)
    '''
    print("Calculating a",int(cl*100),"% CI (z-score)...")
    squared_errors = (pred - test) ** 2
    N=len(squared_errors)
    zscore = stats.norm.ppf((1 + cl) / 2)
    zmargin = zscore * squared_errors.std(ddof=1) / np.sqrt(N)
    np.sqrt(mean - zmargin), np.sqrt(mean + zmargin)


### Print-out functions 

def scores_stats(scroes):
    '''
    Given array for scores, print basic stats 
    '''
    print('scores:',  scroes)
    print("<scores>:", scroes.mean())
    print("𝝈(scores):", scroes.std())

def params_grid(cv_results):
    '''
    Given grid search, print all scores (sorted)
    '''
    # for mean_score, params in zip(cv_results["mean_test_score"], cv_results["params"]):
    dict_results  = sorted(dict(zip(np.sqrt(-cv_results["mean_test_score"]), cv_results["params"])).items())
    for item in dict_results:
        print (item)
