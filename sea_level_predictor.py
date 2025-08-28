import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope1, intercept1, *_ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended1 = np.arange(df['Year'].min(), 2051)
    ax.plot(years_extended1, slope1 * years_extended1 + intercept1)

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, *_ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_extended2 = np.arange(2000, 2051)
    ax.plot(years_extended2, slope2 * years_extended2 + intercept2)

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()