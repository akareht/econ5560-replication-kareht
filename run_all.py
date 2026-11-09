import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels as sm
from statsmodels.discrete.conditional_models import ConditionalLogit
import os

df = pd.read_stata("S1Table.DTA")

#drops participants listed as having not finished
not_finished_index = df[df['finished'] == 0].index
df.drop(index = not_finished_index, inplace=True)

#drops participants who saw the same choice set more than once
unique_choices = df.groupby('id')['choice_variables'].unique()
num_unique = pd.Series((len(v) for v in unique_choices), index=unique_choices.index)
not_complete_id = num_unique[(num_unique == 2) | (num_unique == 3)].index
df[np.isin(df['id'], not_complete_id)]['role'].value_counts()
df_index = df[df['id'].isin(not_complete_id.values)].index
df.drop(df_index, inplace=True)

#reproduce figure 1
treatments = ['Treatment 1', 'Treatment 2', 'Treatment 3']
y_ticks = [0, 5, 10, 15, 20, 25]

fig, ax = plt.subplots(1, 3, figsize=(12, 4))

for i in range(len(treatments)):
    a = df[df['treatment'] == treatments[i]]['choice_variables'].value_counts() / 3
    x = a.index
    y = a.values
    ax[i].bar(x, y)
    ax[i].set_title(treatments[i])
    ax[i].set_xlabel('Choice Variable')
    ax[i].set_xticks(x)
    ax[i].set_yticks(y_ticks)
    ax[i].spines[['right', 'top']].set_visible(False)

folder = 'outputs'
name = 'Figure 1'
path = os.path.join(folder, name)
plt.savefig(path)


#reconstruct interaction terms
df['water_low3'] = df['treatment_3'] * df['wat_low']
df['dev_high23'] = (df['treatment_2'] + df['treatment_3']) * df['dev_high']
df['dev_lim23'] = (df['treatment_2'] + df['treatment_3']) * df['dev_limited']
df['dev_com23'] = (df['treatment_2'] + df['treatment_3']) * df['dev_com']

#consider dev_none, water_high, and cult_none as base cases (drop these to avoid perfect colinearity)
main = ['dev_limited', 'dev_high', 'dev_com', 'wat_med', 'wat_low', 'cult_s', 'cult_sl']
#interaction terms
#was money shown for this attribute
treatment_var = ['dev_lim23', 'dev_high23', 'dev_com23', 'water_med3', 'water_low3']

X = df[main + treatment_var]
y = df['alternative_choice']

#Conditional Logit (All)
model_1 = ConditionalLogit(y, X, groups=df['choice_variables']).fit()

model_1_summary = model_1.summary().as_text()

fig, ax = plt.subplots()
ax.text(0.01, 0.05, model_1_summary, fontfamily='monospace')
ax.axis('off')
name = 'model 1 summary'
path = os.path.join(folder, name)
plt.savefig(path)

#Councillor Only dataframe
df_c = df[df['role'] == 'Councillor']
cX = df_c[main + treatment_var]
cy = df_c['alternative_choice']

#Conditional Logit (Councillor)
model_2 = ConditionalLogit(cy, cX, groups=df_c['choice_variables'])

model_2_summary = model_1.summary().as_text()

fig, ax = plt.subplots()
ax.text(0.01, 0.05, model_2_summary, fontfamily='monospace')
ax.axis('off')
name = 'model 2 summary'
path = os.path.join(folder, name)
plt.savefig(path)
