'''
Author: Gleb Lukicov

Auxiliary functions 
'''

def scores_stats(scroes):
    print('scores:',  scroes)
    print("<scores>:", scroes.mean())
    print("𝝈(scores):", scroes.std())