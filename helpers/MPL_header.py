import matplotlib as mpl
import matplotlib.pyplot as plt
import os
path_to_file= os.path.join(os.environ.get('ML_PATH'),"helpers","ml_style.mplstyle")
plt.style.use('file://'+path_to_file)

#colorbar hacks (non-pandas version)
cbar.ax.tick_params(labelsize=8)
cbar.ax.set_ylabel(fontsize=10)

# mpl.use('Agg') # batch-mode 