import pandas as pd
from scipy.stats import pearsonr


df=pd.read_csv('comparison.csv', header=None)
x=df[0]
y=df[1]

r,p=pearsonr(x,y)
print('Correlation:', r)
print('p-value:', p)

results=pd.DataFrame({'Statistic':['Pearson r','P-value'],
                      'Value':[r,p]})

results.to_csv("comparison_result.csv", index=False)