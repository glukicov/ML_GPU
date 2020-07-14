import matplotlib as mpl
import matplotlib.pyplot as plt
import os
path_to_file= os.path.join(os.environ.get('ML_PATH'),"helpers","ml_style.mplstyle")
plt.style.use('file://'+path_to_file)
# mpl.use('Agg') # batch-mode 