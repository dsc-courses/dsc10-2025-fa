import numpy as np
import babypandas as bpd
import pandas as pd

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rcParams.update({
    'figure.figsize': (10, 5),
    'axes.titlesize': 14,
    'axes.titleweight': 'bold',
    'axes.labelsize': 12,
    'axes.labelweight': 'bold',
    'axes.linewidth': 1.5,
    'grid.color': '#999999',
    'grid.alpha': 0.6,

    # Make all text bold
    'font.weight': 'bold',
    'axes.labelweight': 'bold',
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
    'xtick.major.width': 1.2,
    'ytick.major.width': 1.2,
    'xtick.color': 'black',
    'ytick.color': 'black',
    'legend.fontsize': 11,
    'legend.title_fontsize': 12,
})

np.set_printoptions(threshold=20, precision=2, suppress=True)
pd.set_option("display.max_rows", 7)
pd.set_option("display.max_columns", 8)
pd.set_option("display.precision", 2)

from IPython.display import display, IFrame

def merging_animation():
    src="https://docs.google.com/presentation/d/1d0G-_P6pLWK83wW3wPetGfzLADRqxO3jO0thK7lhtSE/embed?start=false&loop=false&delayms=3000&rm=minimal"
    width=825
    height=500
    display(IFrame(src, width, height))


def concept_check():
    src="https://docs.google.com/presentation/d/1V0d5kNVWmalLY0SkzZzKDDc_3CDZSE5m6Av0gC-PfJo/embed?start=false&loop=false&delayms=3000&rm=minimal"
    width=825
    height=500
    display(IFrame(src, width, height))


