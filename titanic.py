# -*- coding: utf-8 -*-
"""Untitled

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xjrp3lBb0yjrWW4h3x-LunrVxx0JU7mS
"""

from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns


#문제 1번
titanic= sns.load_dataset("titanic")
titanic=titanic.fillna(titanic.mean())
print(titanic)
x,y=np.unique(titanic["age"], return_counts=True)
plt.bar(x,y)
plt.ylabel('count')
plt.xlabel('age')
plt.title("num1 - the number of passenger by age")
plt.show()

#문제 2번
titanic= sns.load_dataset("titanic")
ratio=titanic["alive"].value_counts()
print(titanic["alive"].value_counts())
labels=["death","survivor"]
plt.pie(ratio,labels=labels,autopct='%.1f%%')
plt.title("num2 - survivor ratio")
plt.show()

#문제 3번
titanic= sns.load_dataset("titanic")
titanic=titanic.dropna()
titanic=titanic[titanic["survived"] == 1]
a=titanic[["age","pclass"]].groupby(["pclass"]).mean()
b=titanic["pclass"].sort_values(ascending=True).unique()
print(a)
x=[]
y=[]
for i in range(1,len(a)+1) :
    y.append(a["age"][i])
for i in range(0,len(a)) :
    x.append(b[i])
sns.barplot(x,y)
plt.xlabel('pclass')
plt.ylabel('avg.age')
plt.title("num3 - avg.age by pclass")
plt.show()

#4번
titanic= sns.load_dataset("titanic")
#titanic=titanic.fillna(titanic.mean())
titanic=titanic[titanic["age"]>=20]
titanic=titanic[titanic["survived"]==1]
ratio=titanic["sex"].value_counts()
print(titanic["sex"].value_counts())
labels=["woman","man"]
plt.pie(ratio,labels=labels,autopct='%.1f%%')
plt.title("Ratio of sex of survivor over 20 and ")
plt.title("num4 - survivor ratio by sex")
plt.show()

#문제 5번
titanic= sns.load_dataset("titanic")
titanic=titanic.fillna(titanic.mean())
titanic=titanic[titanic["who"] <= "child"]

a=titanic[(titanic["pclass"]==1) & (titanic["sex"]=="male")]
b=titanic[(titanic["pclass"]==1) & (titanic["sex"]=="female")]
c=titanic[(titanic["pclass"]==2) & (titanic["sex"]=="male")]
d=titanic[(titanic["pclass"]==2) & (titanic["sex"]=="female")]
e=titanic[(titanic["pclass"]==3) & (titanic["sex"]=="male")]
f=titanic[(titanic["pclass"]==3) & (titanic["sex"]=="female")]
x=["xa","xb","xc","xd","xe","xf"]
y=["ya","yb","yc","yd","ye","yf"]
title=["pclass=1,male","pclass=1,female","pclass=2,male","pclass=2,female","pclass=3,male","pclass=3,female"]
plt.bar(x,y)
for i ,alpha in enumerate([a,b,c,d,e,f]) :
    plt.subplot(2, 3, i+1)
    x[i]=np.arange(4)
    y[i]=[alpha["age"].min(),alpha["age"].mean(),alpha["age"].median(),alpha["age"].max()]
    plt.bar(x[i],y[i])
    plt.xticks(x[i],["min","mean","median","max"],fontsize=5)
    plt.title(title[i],fontsize=5)

plt.show()

#문제 6번
titanic= sns.load_dataset("titanic")
titanic=titanic.dropna()
titanic=titanic[titanic["survived"] == 1]
a=titanic[(titanic["fare"]<=100) & (titanic["fare"]>=0)]
print(a["fare"])
b=titanic[(titanic["fare"]<=200) & (titanic["fare"]>=101)]
print(b["fare"])
c=titanic[(titanic["fare"] <= 300) & (titanic["fare"] >= 201)]
print(c["fare"])
d=titanic[(titanic["fare"] >= 301)]
print(d["fare"])
x=[0,1,2,3]
y=[len(a["sex"]),len(b["sex"]),len(c["sex"]),len(d["sex"])]
fare=["0~100","101~200","201~300","301~"]
sns.barplot(x,y)
plt.xlabel('fare')
plt.ylabel('survivor')
plt.xticks(x, fare)

plt.title("num6 - The number of Survivor by fare")
plt.show()