import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = ((df['weight'] / ((df['height'] / 100) ** 2)) > 25).astype(int)

# 3
cols_to_flip = ['cholesterol', 'gluc']
for col in cols_to_flip:
    df[col] = df[col].map(lambda x: 0 if x <= 1 else 1)

# 4
def draw_cat_plot():
    # 5
    df_cat = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    plot_df = pd.melt(df,
                      id_vars='cardio',
                      value_vars=df_cat,
                      var_name='variable',
                      value_name='value')
    grouped_df = (
        plot_df
        .groupby(['cardio', 'variable', 'value'])
        .size()
        .reset_index(name='total')
    )

    # 7
    g=sns.catplot(
        data=grouped_df,
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        kind='bar'
    )

    # 8
    fig = g.figure

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
    (df['ap_lo'] <= df['ap_hi']) &
    (df['height'] >= df['height'].quantile(0.025)) &
    (df['height'] <= df['height'].quantile(0.975)) &
    (df['weight'] >= df['weight'].quantile(0.025)) &
    (df['weight'] <= df['weight'].quantile(0.975))
    ].copy()

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots()

    # 15
    sns.heatmap(corr,
                mask=mask,
                annot=True,
                fmt='.1f',
                vmin=-0.08,
                vmax=0.24,
                center=0,
                ax=ax)

    # 16
    fig.savefig('heatmap.png')
    return fig
