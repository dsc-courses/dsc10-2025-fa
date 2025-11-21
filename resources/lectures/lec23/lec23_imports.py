import numpy as np
import babypandas as bpd
import pandas as pd

import matplotlib.pyplot as plt
plt.style.use('seaborn-colorblind')
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

green = (0.0, 0.6196078431372549, 0.45098039215686275)
orange = (0.8352941176470589, 0.3686274509803922, 0.0)
gold = (0.9411764705882353, 0.8941176470588236, 0.25882352941176473)
pink = (0.8, 0.4745098039215686, 0.6549019607843137)
np.set_printoptions(threshold=20, precision=2, suppress=True)
pd.set_option("display.max_rows", 7)
pd.set_option("display.max_columns", 8)
pd.set_option("display.precision", 2)

import warnings
warnings.filterwarnings('ignore')

# Demonstration code
from IPython.display import display
import ipywidgets as widgets
import plotly.express as px

def r_scatter(r):
    "Generate a scatter plot with a correlation approximately r"
    x = np.random.normal(0, 1, 1000)
    z = np.random.normal(0, 1, 1000)
    y = r * x + (np.sqrt(1 - r ** 2)) * z
    plt.scatter(x, y)
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)
    plt.title(f'$r={r}$')
    
def show_scatter_grid():
    plt.subplots(1, 4, figsize=(10, 2))
    for i, r in enumerate([-1, -2/3, -1/3, 0]):
        plt.subplot(1, 4, i+1)
        r_scatter(r)
        plt.title(f'r = {np.round(r, 2)}')
    plt.show()
    plt.subplots(1, 4, figsize=(10, 2))
    for i, r in enumerate([1, 2/3, 1/3]):
        plt.subplot(1, 4, i+1)
        r_scatter(r)
        plt.title(f'$r = {np.round(r, 2)}$')
    plt.subplot(1, 4, 4)
    plt.axis('off')
    plt.show()