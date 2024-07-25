import numpy as np
import scipy as sp
import matplotlib as mpl
import time
import sys

# Create a dictionary with module names and their versions
modules = {
    'numpy': np.__version__,
    'scipy': sp.__version__,
    'matplotlib': mpl.__version__,
    'time': time.__doc__,  # 'time' module does not have a version attribute
    'python': sys.version  # Python version
}

# Write the module versions to a text file
with open('../documentation/module_versions.txt', 'w') as f:
    for module, version in modules.items():
        f.write(f'{module}: {version}\n')

print("Module versions have been written to '../documentation/module_versions.txt'.")

#%%
