import matplotlib as mpl
import matplotlib.pyplot as plt
import os
# mpl.use('Agg') # batch-mode 
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)
# plt.style.use('fivethirtyeight')
# plt.style.use('dark_background')
path_to_file= os.path.join(os.environ.get('ML_PATH'),"helpers","ml_style.mplstyle")
plt.style.use('file://'+path_to_file)

# mpl.rc('color', 'green')
# mpl.rc('grid', False)