import recsys.algorithm
recsys.algorithm.VERBOSE = True

from recsys.algorithm.factorize import SVD
svd = SVD()
svd.load_data(filename='ml-1m/ratings.dat', sep='::', format={'col':0, 'row':1, 'value':2, 'ids': int})