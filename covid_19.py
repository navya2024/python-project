import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import subprocess


df = pd.read_csv('B:\Project-python\covid_19_india.csv')
hf = df.head(300)
print(hf)
plt.figure(figsize=(10,10))
plt.xticks(rotation=70)
sns.scatterplot(x='State/UnionTerritory',y='ConfirmedIndianNational',data=hf ,size=3, palette="YlWhBu")
plt.title("Covid Confirmed Indian Cases State wise", size=20, family='cursive',color='black',loc='center')
plt.savefig('img1.png',format='png')

plt.figure(figsize=[10,10])
plt.xticks(rotation=70)
sns.histplot(x='State/UnionTerritory',y='ConfirmedForeignNational',data=hf,bins=30)
plt.title("Covid Confirmed Foregin Cases State wise", size=30, family='cursive',color='cyan',loc='center')
plt.savefig('img2.png',format='png')



plt.figure(figsize=(10,10))
plt.xticks(rotation=70)
sns.boxplot(x='State/UnionTerritory',y='Confirmed',data=hf,palette="YlGnBu")
plt.title("Covid Cases Confirmed State wise", size=30,family='cursive',color='green',fontstyle='italic',loc='center')
plt.savefig('img3.png',format='png')

plt.figure(figsize=(10,10))
plt.xticks(rotation=70)
sns.boxplot(x='State/UnionTerritory',y="Deaths", data=hf,palette="YlGnBu")
plt.title("Covid Death Cases State wise ", size=30, family='cursive',color='red',loc='center')
plt.savefig('img4.png',format='png')




plt.figure(figsize=(10,10))
sns.stripplot(x='Cured',y='Deaths',data=hf,dodge=True,palette="YlGnBu")
plt.title("Cured VS Deaths Cases in India  ", size=30, family='cursive',color='purple',loc='center')
plt.savefig('img5.png',format='png')



plt.figure(figsize=[10,10])
sns.jointplot(x="Cured",y="Confirmed",data=hf,kind="kde",shades=True,cmap="YlGnBu")
plt.savefig('img6.png',format='png')


plt.figure(figsize=[10,10])
x=df['ConfirmedIndianNational']
y=df['Cured']
plt.xticks(rotation=90)
plt.title("Indian Cured Cases in India  ", size=30, family='cursive',color='purple',loc='center')
plt.bar(y,color="purple",width=20,height=9,label='p=Cured')
plt.savefig('img7.png',format='png')

plt.figure(figsize=[20,10])
x=df['ConfirmedIndianNational']
y=df['Deaths']
plt.xlabel('ConfirmedIndianNational', fontsize=18)
plt.ylabel('Deaths', fontsize=18)
plt.hist(y,color='green',rwidth=0.9,alpha=0.3,bins=20,label='b=Deaths')
plt.title("Indian Cured VS Deaths Cases in India ", size=30, family='cursive',color='cyan',loc='center')
plt.savefig('img8.png',format='png')

sns.heatmap(hf.corr(),annot=True,cmap="YlGnBu")
plt.savefig('img9.png',format='png')


subprocess.call("show-tk.py", shell=True)