import pandas as pd
from matplotlib import pyplot as plt

f=pd.read_csv('Countries Data.csv')
f.dropna()
print(f.head(10))

plt.bar(f['year'], f['population'], width=2)
plt.grid(True)

plt.show()
c52=f.loc[f['year']==1952]
c7=f.loc[f['year']==2007]
x=c52.merge(c7, left_on='country', right_on='country')
print(x)
x['population_growth']=x['population_y']-x['population_x']

x=x.sort_values('population_growth', ascending=False).head(10)

n=['China', 'India', 'United States', 'Indonesia', 'Brazil', 'Pakistan', 'Bangladesh', 'Nigeria', 'Mexico', 'Philippines']
pg=x['population_growth']/10**6
plt.bar(n,pg,width=4)
plt.grid(True)
plt.xticks(rotation=45)
for x,y in zip(n,pg):
    label="{:.2f}".format(y)
    plt.annotate(label,(x,y), textcoords="offset points", xytext=(0,10), ha='center')

plt.show()