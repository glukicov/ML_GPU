"""e
Author: Gleb Lukicov

Auxiliary functions
"""
from sklearn.model_selection import StratifiedKFold 
from sklearn.base import clone
import numpy as np 
from scipy import stats

### Stat functions

def ci(pred, test, cl=0.95):
    """
    t-score CI
    """
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


### Ease-of-life
def save_fig(fig_path=".", fig_id="0", fig_extension="png", tight_layout=True, resolution=300):
    path = os.path.join(fig_path, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)


### ML functions


def misc_cross_val_score(X_train, y_train, sgd_clf, cv=3):
    """
    #  Implimentation of the cross_val_score function
    # Crdeit: https://github.com/ageron/handson-ml2 
    The StratifiedKFold class performs stratified sampling,
    to produce folds that contain a representative ratio of each class. 
    At each iteration the code creates a clone of the classifier, 
    trains that clone on the training folds, and makes predictions on the test fold. 
    Then it counts the number of correct predictions and outputs the ratio of correct predictions.
    """
    skfolds = StratifiedKFold(n_splits=cv, random_state=42)
    for train_index, test_index in skfolds.split(X_train, y_train):
        clone_clf = clone(sgd_clf)
        X_train_folds = X_train[train_index]
        y_train_folds = y_train[train_index]
        X_test_fold = X_train[test_index] y_test_fold = y_train[test_index]
        clone_clf.fit(X_train_folds, y_train_folds)
        y_pred = clone_clf.predict(X_test_fold)
        n_correct = sum(y_pred == y_test_fold)
        print(n_correct / len(y_pred))  # prints e.g. 0.9502, 0.96565, and 0.96495


