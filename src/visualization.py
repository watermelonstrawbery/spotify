import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def bar_chart(df, filename, title):
    df.plot(kind='bar')
    plt.title(title)
    plt.ylabel('popularity')
    plt.tight_layout()
    plt.savefig(f'../output/chart/{filename}')
