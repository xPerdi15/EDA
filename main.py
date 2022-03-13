import pandas as pd
import json 
import openpyxl
from sklearn.datasets import load_iris, load_boston
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
sns.set(style="darkgrid")
#vamos a importar todos los datasets
#2012-13:
df_laliga_2012y13 = pd.read_csv('espana-master/2010s/2012-13/es.1.csv')
df_laliga_2012y13
new = df_laliga_2012y13['FT'].str.split('-',n=1,expand=True)
df_laliga_2012y13['GolesLocal']=new[0]
df_laliga_2012y13['GolesVisitante']=new[1]
df_laliga_2012y13
df_laliga_2012y13['GolesLocal']=pd.to_numeric(df_laliga_2012y13['GolesLocal'], downcast="float")
df_laliga_2012y13['GolesVisitante']=pd.to_numeric(df_laliga_2012y13['GolesVisitante'], downcast="float")

df_laliga_2012y13['TotalGolesPartido'] = df_laliga_2012y13['GolesLocal']+df_laliga_2012y13['GolesVisitante']
df_laliga_2012y13
#2013-14
df_laliga_2013y14 = pd.read_csv('espana-master/2010s/2013-14/es.1.csv')
new = df_laliga_2013y14['FT'].str.split('-',n=1,expand=True)
df_laliga_2013y14['GolesLocal']=new[0]
df_laliga_2013y14['GolesVisitante']=new[1]
df_laliga_2013y14
#Convertimos en float los goles para poder trabajar con ellos y creamos columna goles totales por partido
df_laliga_2013y14['GolesLocal']=pd.to_numeric(df_laliga_2013y14['GolesLocal'], downcast="float")
df_laliga_2013y14['GolesVisitante']=pd.to_numeric(df_laliga_2013y14['GolesVisitante'], downcast="float")
#Esta columna se usará al final del EDA para comparar cada año de la Liga
df_laliga_2013y14['TotalGolesPartido'] = df_laliga_2013y14['GolesLocal']+df_laliga_2013y14['GolesVisitante']
df_laliga_2013y14

#2014-15
df_laliga_2014y15 = pd.read_csv('espana-master/2010s/2014-15/es.1.csv')
new = df_laliga_2014y15['FT'].str.split('-',n=1,expand=True)
df_laliga_2014y15['GolesLocal']=new[0]
df_laliga_2014y15['GolesVisitante']=new[1]
df_laliga_2014y15

df_laliga_2014y15['GolesLocal']=pd.to_numeric(df_laliga_2014y15['GolesLocal'], downcast="float")
df_laliga_2014y15['GolesVisitante']=pd.to_numeric(df_laliga_2014y15['GolesVisitante'], downcast="float")
df_laliga_2014y15['TotalGolesPartido'] = df_laliga_2014y15['GolesLocal']+df_laliga_2014y15['GolesVisitante']
df_laliga_2014y15

#2015-16
df_laliga_2015y16 = pd.read_csv('espana-master/2010s/2015-16/es.1.csv')
new = df_laliga_2015y16['FT'].str.split('-',n=1,expand=True)
df_laliga_2015y16['GolesLocal']=new[0]
df_laliga_2015y16['GolesVisitante']=new[1]
df_laliga_2015y16

df_laliga_2015y16['GolesLocal']=pd.to_numeric(df_laliga_2015y16['GolesLocal'], downcast="float")
df_laliga_2015y16['GolesVisitante']=pd.to_numeric(df_laliga_2015y16['GolesVisitante'], downcast="float")
df_laliga_2015y16['TotalGolesPartido'] = df_laliga_2015y16['GolesLocal']+df_laliga_2015y16['GolesVisitante']
df_laliga_2015y16

#2016-17
df_laliga_2016y17 = pd.read_csv('espana-master/2010s/2016-17/es.1.csv')
new = df_laliga_2016y17['FT'].str.split('-',n=1,expand=True)
df_laliga_2016y17['GolesLocal']=new[0]
df_laliga_2016y17['GolesVisitante']=new[1]
df_laliga_2016y17

df_laliga_2016y17['GolesLocal']=pd.to_numeric(df_laliga_2016y17['GolesLocal'], downcast="float")
df_laliga_2016y17['GolesVisitante']=pd.to_numeric(df_laliga_2016y17['GolesVisitante'], downcast="float")
df_laliga_2016y17['TotalGolesPartido'] = df_laliga_2016y17['GolesLocal']+df_laliga_2016y17['GolesVisitante']
df_laliga_2016y17

#2017-18
df_laliga_2017y18 = pd.read_csv('espana-master/2010s/2017-18/es.1.csv')
new = df_laliga_2017y18['FT'].str.split('-',n=1,expand=True)
df_laliga_2017y18['GolesLocal']=new[0]
df_laliga_2017y18['GolesVisitante']=new[1]
df_laliga_2017y18

df_laliga_2017y18['GolesLocal']=pd.to_numeric(df_laliga_2017y18['GolesLocal'], downcast="float")
df_laliga_2017y18['GolesVisitante']=pd.to_numeric(df_laliga_2017y18['GolesVisitante'], downcast="float")
df_laliga_2017y18['TotalGolesPartido'] = df_laliga_2017y18['GolesLocal']+df_laliga_2017y18['GolesVisitante']
df_laliga_2017y18

#2018-19
df_laliga_2018y19 = pd.read_csv('espana-master/2010s/2018-19/es.1.csv')
new = df_laliga_2018y19['FT'].str.split('-',n=1,expand=True)
df_laliga_2018y19['GolesLocal']=new[0]
df_laliga_2018y19['GolesVisitante']=new[1]
df_laliga_2018y19

df_laliga_2018y19['GolesLocal']=pd.to_numeric(df_laliga_2018y19['GolesLocal'], downcast="float")
df_laliga_2018y19['GolesVisitante']=pd.to_numeric(df_laliga_2018y19['GolesVisitante'], downcast="float")
df_laliga_2018y19['TotalGolesPartido'] = df_laliga_2018y19['GolesLocal']+df_laliga_2018y19['GolesVisitante']
df_laliga_2018y19

#2019-20
df_laliga_2019y20 = pd.read_csv('espana-master/2010s/2019-20/es.1.csv')
new = df_laliga_2019y20['FT'].str.split('-',n=1,expand=True)
df_laliga_2019y20['GolesLocal']=new[0]
df_laliga_2019y20['GolesVisitante']=new[1]
df_laliga_2019y20
df_laliga_2019y20['GolesLocal']=pd.to_numeric(df_laliga_2019y20['GolesLocal'], downcast="float")
df_laliga_2019y20['GolesVisitante']=pd.to_numeric(df_laliga_2019y20['GolesVisitante'], downcast="float")
df_laliga_2019y20['TotalGolesPartido'] = df_laliga_2019y20['GolesLocal']+df_laliga_2019y20['GolesVisitante']
df_laliga_2019y20

#Ahora vamos a sacar los datasets por equipo (principalmente Madrid y Barcelona salvo una temporada que se incluye al Atlético de Madrid)

#Madrid y Barcelona 2012-13
BarsaL_1 = df_laliga_2012y13.loc[df_laliga_2012y13['Team 1'] == 'FC Barcelona', ['GolesLocal']]
BarsaL_1.reset_index(inplace=True)

BarsaV_1 = df_laliga_2012y13.loc[df_laliga_2012y13['Team 2'] == 'FC Barcelona', ['GolesVisitante']]
BarsaV_1.reset_index(inplace=True)

BarsaTot_1=pd.merge(BarsaL_1, BarsaV_1, left_index=True, right_index=True)
BarsaTot_1['GolesTotales']=BarsaTot_1['GolesLocal']+BarsaTot_1['GolesVisitante']

RealMadridL_1 = df_laliga_2012y13.loc[df_laliga_2012y13['Team 1'] == 'Real Madrid', ['GolesLocal']]
RealMadridL_1.reset_index(inplace=True)

RealMadridV_1 = df_laliga_2012y13.loc[df_laliga_2012y13['Team 2'] == 'Real Madrid', ['GolesVisitante']]
RealMadridV_1.reset_index(inplace=True)

Madrid_Tot_1=pd.merge(RealMadridL_1, RealMadridV_1, left_index=True, right_index=True)
Madrid_Tot_1['GolesTotales']=Madrid_Tot_1['GolesLocal']+Madrid_Tot_1['GolesVisitante']

#Madrid, Barcelona y Atlético de Madrid 2013-14
AtletiL_1=df_laliga_2013y14.loc[df_laliga_2013y14['Team 1'] == 'Atlético Madrid', ['GolesLocal']]
AtletiL_1.reset_index(inplace=True)

AtletiV_1=df_laliga_2013y14.loc[df_laliga_2013y14['Team 2'] == 'Atlético Madrid', ['GolesVisitante']]
AtletiV_1.reset_index(inplace=True)

Atleti_Tot_1=pd.merge(AtletiL_1, AtletiV_1, left_index=True, right_index=True)
Atleti_Tot_1['GolesTotales']=Atleti_Tot_1['GolesLocal']+Atleti_Tot_1['GolesVisitante']

RealMadridL_2 = df_laliga_2013y14.loc[df_laliga_2013y14['Team 1'] == 'Real Madrid', ['GolesLocal']]
RealMadridL_2.reset_index(inplace=True)

RealMadridV_2 = df_laliga_2013y14.loc[df_laliga_2013y14['Team 2'] == 'Real Madrid', ['GolesVisitante']]
RealMadridV_2.reset_index(inplace=True)

Madrid_Tot_2=pd.merge(RealMadridL_2, RealMadridV_2, left_index=True, right_index=True)
Madrid_Tot_2['GolesTotales']=Madrid_Tot_2['GolesLocal']+Madrid_Tot_2['GolesVisitante']

BarsaL_2 = df_laliga_2013y14.loc[df_laliga_2013y14['Team 1'] == 'FC Barcelona', ['GolesLocal']]
BarsaL_2.reset_index(inplace=True)

BarsaV_2 = df_laliga_2013y14.loc[df_laliga_2013y14['Team 2'] == 'FC Barcelona', ['GolesVisitante']]
BarsaV_2.reset_index(inplace=True)

BarsaTot_2=pd.merge(BarsaL_2, BarsaV_2, left_index=True, right_index=True)
BarsaTot_2['GolesTotales']=BarsaTot_2['GolesLocal']+BarsaTot_2['GolesVisitante']

#Madrid y Barcelona 2014-15
BarsaL_3 = df_laliga_2014y15.loc[df_laliga_2014y15['Team 1'] == 'FC Barcelona', ['GolesLocal']]
BarsaL_3.reset_index(inplace=True)

BarsaV_3 = df_laliga_2014y15.loc[df_laliga_2014y15['Team 2'] == 'FC Barcelona', ['GolesVisitante']]
BarsaV_3.reset_index(inplace=True)

BarsaTot_3=pd.merge(BarsaL_3, BarsaV_3, left_index=True, right_index=True)
BarsaTot_3['GolesTotales']=BarsaTot_3['GolesLocal']+BarsaTot_3['GolesVisitante']

RealMadridL_3 = df_laliga_2014y15.loc[df_laliga_2014y15['Team 1'] == 'Real Madrid', ['GolesLocal']]
RealMadridL_3.reset_index(inplace=True)

RealMadridV_3 = df_laliga_2014y15.loc[df_laliga_2014y15['Team 2'] == 'Real Madrid', ['GolesVisitante']]
RealMadridV_3.reset_index(inplace=True)

Madrid_Tot_3=pd.merge(RealMadridL_3, RealMadridV_3, left_index=True, right_index=True)
Madrid_Tot_3['GolesTotales']=Madrid_Tot_3['GolesLocal']+Madrid_Tot_3['GolesVisitante']

#Madrid y Barcelona 2015-16
BarsaL_4 = df_laliga_2015y16.loc[df_laliga_2015y16['Team 1'] == 'FC Barcelona', ['GolesLocal']]
BarsaL_4.reset_index(inplace=True)

BarsaV_4 = df_laliga_2015y16.loc[df_laliga_2015y16['Team 2'] == 'FC Barcelona', ['GolesVisitante']]
BarsaV_4.reset_index(inplace=True)

BarsaTot_4=pd.merge(BarsaL_4, BarsaV_4, left_index=True, right_index=True)
BarsaTot_4['GolesTotales']=BarsaTot_4['GolesLocal']+BarsaTot_4['GolesVisitante']

RealMadridL_4 = df_laliga_2015y16.loc[df_laliga_2015y16['Team 1'] == 'Real Madrid', ['GolesLocal']]
RealMadridL_4.reset_index(inplace=True)

RealMadridV_4 = df_laliga_2015y16.loc[df_laliga_2015y16['Team 2'] == 'Real Madrid', ['GolesVisitante']]
RealMadridV_4.reset_index(inplace=True)

Madrid_Tot_4=pd.merge(RealMadridL_4, RealMadridV_4, left_index=True, right_index=True)
Madrid_Tot_4['GolesTotales']=Madrid_Tot_4['GolesLocal']+Madrid_Tot_4['GolesVisitante']

#Madrid y Barcelona 2016-17
BarsaL_5 = df_laliga_2016y17.loc[df_laliga_2016y17['Team 1'] == 'FC Barcelona', ['GolesLocal']]
BarsaL_5.reset_index(inplace=True)

BarsaV_5 = df_laliga_2016y17.loc[df_laliga_2016y17['Team 2'] == 'FC Barcelona', ['GolesVisitante']]
BarsaV_5.reset_index(inplace=True)

BarsaTot_5=pd.merge(BarsaL_5, BarsaV_5, left_index=True, right_index=True)
BarsaTot_5['GolesTotales']=BarsaTot_5['GolesLocal']+BarsaTot_5['GolesVisitante']

RealMadridL_5 = df_laliga_2016y17.loc[df_laliga_2016y17['Team 1'] == 'Real Madrid', ['GolesLocal']]
RealMadridL_5.reset_index(inplace=True)

RealMadridV_5 = df_laliga_2016y17.loc[df_laliga_2016y17['Team 2'] == 'Real Madrid', ['GolesVisitante']]
RealMadridV_5.reset_index(inplace=True)

Madrid_Tot_5=pd.merge(RealMadridL_5, RealMadridV_5, left_index=True, right_index=True)
Madrid_Tot_5['GolesTotales']=Madrid_Tot_5['GolesLocal']+Madrid_Tot_5['GolesVisitante']

#Madrid y Barcelona 2017-18
BarsaL_6 = df_laliga_2017y18.loc[df_laliga_2017y18['Team 1'] == 'FC Barcelona', ['GolesLocal']]
BarsaL_6.reset_index(inplace=True)

BarsaV_6 = df_laliga_2017y18.loc[df_laliga_2017y18['Team 2'] == 'FC Barcelona', ['GolesVisitante']]
BarsaV_6.reset_index(inplace=True)

BarsaTot_6=pd.merge(BarsaL_6, BarsaV_6, left_index=True, right_index=True)
BarsaTot_6['GolesTotales']=BarsaTot_6['GolesLocal']+BarsaTot_6['GolesVisitante']

RealMadridL_6 = df_laliga_2017y18.loc[df_laliga_2017y18['Team 1'] == 'Real Madrid', ['GolesLocal']]
RealMadridL_6.reset_index(inplace=True)

RealMadridV_6 = df_laliga_2017y18.loc[df_laliga_2017y18['Team 2'] == 'Real Madrid', ['GolesVisitante']]
RealMadridV_6.reset_index(inplace=True)

Madrid_Tot_6=pd.merge(RealMadridL_6, RealMadridV_6, left_index=True, right_index=True)
Madrid_Tot_6['GolesTotales']=Madrid_Tot_6['GolesLocal']+Madrid_Tot_6['GolesVisitante']

#Madrid y Barcelona 2018-19
BarsaL_7 = df_laliga_2018y19.loc[df_laliga_2018y19['Team 1'] == 'FC Barcelona', ['GolesLocal']]
BarsaL_7.reset_index(inplace=True)

BarsaV_7 = df_laliga_2018y19.loc[df_laliga_2018y19['Team 2'] == 'FC Barcelona', ['GolesVisitante']]
BarsaV_7.reset_index(inplace=True)

BarsaTot_7=pd.merge(BarsaL_7, BarsaV_7, left_index=True, right_index=True)
BarsaTot_7['GolesTotales']=BarsaTot_7['GolesLocal']+BarsaTot_7['GolesVisitante']

RealMadridL_7 = df_laliga_2018y19.loc[df_laliga_2018y19['Team 1'] == 'Real Madrid', ['GolesLocal']]
RealMadridL_7.reset_index(inplace=True)

RealMadridV_7 = df_laliga_2018y19.loc[df_laliga_2018y19['Team 2'] == 'Real Madrid', ['GolesVisitante']]
RealMadridV_7.reset_index(inplace=True)

Madrid_Tot_7=pd.merge(RealMadridL_7, RealMadridV_7, left_index=True, right_index=True)
Madrid_Tot_7['GolesTotales']=Madrid_Tot_7['GolesLocal']+Madrid_Tot_7['GolesVisitante']

#Madrid y Barcelona 2019-20
BarsaL_8 = df_laliga_2019y20.loc[df_laliga_2019y20['Team 1'] == 'FC Barcelona', ['GolesLocal']]
BarsaL_8.reset_index(inplace=True)

BarsaV_8 = df_laliga_2019y20.loc[df_laliga_2019y20['Team 2'] == 'FC Barcelona', ['GolesVisitante']]
BarsaV_8.reset_index(inplace=True)

BarsaTot_8=pd.merge(BarsaL_8, BarsaV_8, left_index=True, right_index=True)
BarsaTot_8['GolesTotales']=BarsaTot_8['GolesLocal']+BarsaTot_8['GolesVisitante']

RealMadridL_8 = df_laliga_2019y20.loc[df_laliga_2019y20['Team 1'] == 'Real Madrid', ['GolesLocal']]
RealMadridL_8.reset_index(inplace=True)

RealMadridV_8 = df_laliga_2019y20.loc[df_laliga_2019y20['Team 2'] == 'Real Madrid', ['GolesVisitante']]
RealMadridV_8.reset_index(inplace=True)

Madrid_Tot_8=pd.merge(RealMadridL_8, RealMadridV_8, left_index=True, right_index=True)
Madrid_Tot_8['GolesTotales']=Madrid_Tot_8['GolesLocal']+Madrid_Tot_8['GolesVisitante']

#Ahora empezamos con las visualizaciones
#Este gráfico nos muestra goles por partido y total de partidos con esa cantidad de goles
plt.figure(figsize=(10,5))
sns.distplot(df_laliga_2012y13['TotalGolesPartido'],
             kde=False,
             color='g',
             bins=50);

plt.figure(figsize=(10,5))
sns.distplot(df_laliga_2013y14['TotalGolesPartido'],
             kde=False,
             color='g',
             bins=50);

plt.figure(figsize=(10,5))
sns.distplot(df_laliga_2014y15['TotalGolesPartido'],
             kde=False,
             color='g',
             bins=50);

plt.figure(figsize=(10,5))
sns.distplot(df_laliga_2015y16['TotalGolesPartido'],
             kde=False,
             color='g',
             bins=50);

plt.figure(figsize=(10,5))
sns.distplot(df_laliga_2016y17['TotalGolesPartido'],
             kde=False,
             color='g',
             bins=50);

plt.figure(figsize=(10,5))
sns.distplot(df_laliga_2017y18['TotalGolesPartido'],
             kde=False,
             color='g',
             bins=50);

plt.figure(figsize=(10,5))
sns.distplot(df_laliga_2018y19['TotalGolesPartido'],
             kde=False,
             color='g',
             bins=50);

plt.figure(figsize=(10,5))
sns.distplot(df_laliga_2019y20['TotalGolesPartido'],
             kde=False,
             color='g',
             bins=50);
#Gráficos de violín de goles como local y partidos con esos goles de todos los equipos de LaLiga por temporada
plt.figure(figsize=(40,15))
sns.violinplot(x=df_laliga_2012y13['Team 1'].sort_values(), y=df_laliga_2012y13['GolesLocal'])

plt.figure(figsize=(40,15))
sns.violinplot(x=df_laliga_2013y14['Team 1'].sort_values(), y=df_laliga_2012y13['GolesLocal'])

plt.figure(figsize=(40,15))
sns.violinplot(x=df_laliga_2014y15['Team 1'].sort_values(), y=df_laliga_2012y13['GolesLocal'])

plt.figure(figsize=(40,15))
sns.violinplot(x=df_laliga_2015y16['Team 1'].sort_values(), y=df_laliga_2012y13['GolesLocal'])

plt.figure(figsize=(40,15))
sns.violinplot(x=df_laliga_2016y17['Team 1'].sort_values(), y=df_laliga_2012y13['GolesLocal'])

plt.figure(figsize=(40,15))
sns.violinplot(x=df_laliga_2017y18['Team 1'].sort_values(), y=df_laliga_2012y13['GolesLocal'])

plt.figure(figsize=(40,15))
sns.violinplot(x=df_laliga_2018y19['Team 1'].sort_values(), y=df_laliga_2012y13['GolesLocal'])

plt.figure(figsize=(40,15))
sns.violinplot(x=df_laliga_2019y20['Team 1'].sort_values(), y=df_laliga_2012y13['GolesLocal'])

#Gráficos de violín de goles como visitante y partidos con esos goles de todos los equipos de LaLiga por temporada
plt.figure(figsize=(40,15))
sns.violinplot(x=df_laliga_2012y13['Team 2'].sort_values(), y=df_laliga_2012y13['GolesVisitante'])

plt.figure(figsize=(40,15))
sns.violinplot(x=df_laliga_2013y14['Team 2'].sort_values(), y=df_laliga_2012y13['GolesVisitante'])

plt.figure(figsize=(40,15))
sns.violinplot(x=df_laliga_2014y15['Team 2'].sort_values(), y=df_laliga_2012y13['GolesVisitante'])

plt.figure(figsize=(40,15))
sns.violinplot(x=df_laliga_2015y16['Team 2'].sort_values(), y=df_laliga_2012y13['GolesVisitante'])

plt.figure(figsize=(40,15))
sns.violinplot(x=df_laliga_2016y17['Team 2'].sort_values(), y=df_laliga_2012y13['GolesVisitante'])

plt.figure(figsize=(40,15))
sns.violinplot(x=df_laliga_2017y18['Team 2'].sort_values(), y=df_laliga_2012y13['GolesVisitante'])

plt.figure(figsize=(40,15))
sns.violinplot(x=df_laliga_2018y19['Team 2'].sort_values(), y=df_laliga_2012y13['GolesVisitante'])

plt.figure(figsize=(40,15))
sns.violinplot(x=df_laliga_2019y20['Team 2'].sort_values(), y=df_laliga_2012y13['GolesVisitante'])

#Evolución Real Madrid CF vs FC Barcelona 2012-2020 como local 
plt.figure(figsize = (20,10))
sns.distplot(Madrid_Tot_1['GolesLocal'],kde=False, label='Madrid como local')
sns.distplot(BarsaTot_1['GolesLocal'],kde=False, label='Barsa como local')
plt.title("2012-13 Madrid local vs Barsa local")
plt.legend()

plt.figure(figsize = (20,10))
sns.distplot(Madrid_Tot_2['GolesLocal'],kde=False, label='Madrid como local')
sns.distplot(BarsaTot_2['GolesLocal'],kde=False, label='Barsa como local')
plt.title("2013-14 Madrid local vs Barsa local")
plt.legend()

plt.figure(figsize = (20,10))
sns.distplot(Madrid_Tot_3['GolesLocal'],kde=False, label='Madrid como local')
sns.distplot(BarsaTot_3['GolesLocal'],kde=False, label='Barsa como local')
plt.title("2014-15 Madrid local vs Barsa local")
plt.legend()

plt.figure(figsize = (20,10))
sns.distplot(Madrid_Tot_4['GolesLocal'],kde=False, label='Madrid como local')
sns.distplot(BarsaTot_4['GolesLocal'],kde=False, label='Barsa como local')
plt.title("2015-16 Madrid local vs Barsa local")
plt.legend()

plt.figure(figsize = (20,10))
sns.distplot(Madrid_Tot_5['GolesLocal'],kde=False, label='Madrid como local')
sns.distplot(BarsaTot_5['GolesLocal'],kde=False, label='Barsa como local')
plt.title("2016-17 Madrid local vs Barsa local")
plt.legend()

plt.figure(figsize = (20,10))
sns.distplot(Madrid_Tot_6['GolesLocal'],kde=False, label='Madrid como local')
sns.distplot(BarsaTot_6['GolesLocal'],kde=False, label='Barsa como local')
plt.title("2017-18 Madrid local vs Barsa local")
plt.legend()

plt.figure(figsize = (20,10))
sns.distplot(Madrid_Tot_7['GolesLocal'],kde=False, label='Madrid como local')
sns.distplot(BarsaTot_7['GolesLocal'],kde=False, label='Barsa como local')
plt.title("2018-19 Madrid local vs Barsa local")
plt.legend()

plt.figure(figsize = (20,10))
sns.distplot(Madrid_Tot_8['GolesLocal'],kde=False, label='Madrid como local')
sns.distplot(BarsaTot_8['GolesLocal'],kde=False, label='Barsa como local')
plt.title("2019-20 Madrid local vs Barsa local")
plt.legend()

#Evolución Real Madrid CF vs FC Barcelona 2012-2020 como visitantes
plt.figure(figsize = (20,10))
sns.distplot(Madrid_Tot_1['GolesVisitante'],kde=False, label='Madrid como visitante')
sns.distplot(BarsaTot_1['GolesVisitante'],kde=False, label='Barsa como visitante')
plt.title("2012-13 Madrid visitante vs Barsa visitante")
plt.legend()

plt.figure(figsize = (20,10))
sns.distplot(Madrid_Tot_2['GolesVisitante'],kde=False, label='Madrid como visitante')
sns.distplot(BarsaTot_2['GolesVisitante'],kde=False, label='Barsa como visitante')
plt.title("2013-14 Madrid visitante vs Barsa visitante")
plt.legend()

plt.figure(figsize = (20,10))
sns.distplot(Madrid_Tot_3['GolesVisitante'],kde=False, label='Madrid como visitante')
sns.distplot(BarsaTot_3['GolesVisitante'],kde=False, label='Barsa como visitante')
plt.title("2014-15 Madrid visitante vs Barsa visitante")
plt.legend()

plt.figure(figsize = (20,10))
sns.distplot(Madrid_Tot_4['GolesVisitante'],kde=False, label='Madrid como visitante')
sns.distplot(BarsaTot_4['GolesVisitante'],kde=False, label='Barsa como visitante')
plt.title("2015-16 Madrid visitante vs Barsa visitante")
plt.legend()

plt.figure(figsize = (20,10))
sns.distplot(Madrid_Tot_5['GolesVisitante'],kde=False, label='Madrid como visitante')
sns.distplot(BarsaTot_5['GolesVisitante'],kde=False, label='Barsa como visitante')
plt.title("2016-17 Madrid visitante vs Barsa visitante")
plt.legend()

plt.figure(figsize = (20,10))
sns.distplot(Madrid_Tot_6['GolesVisitante'],kde=False, label='Madrid como visitante')
sns.distplot(BarsaTot_6['GolesVisitante'],kde=False, label='Barsa como visitante')
plt.title("2017-18 Madrid visitante vs Barsa visitante")
plt.legend()

plt.figure(figsize = (20,10))
sns.distplot(Madrid_Tot_7['GolesVisitante'],kde=False, label='Madrid como visitante')
sns.distplot(BarsaTot_7['GolesVisitante'],kde=False, label='Barsa como visitante')
plt.title("2018-19 Madrid visitante vs Barsa visitante")
plt.legend()

plt.figure(figsize = (20,10))
sns.distplot(Madrid_Tot_8['GolesVisitante'],kde=False, label='Madrid como visitante')
sns.distplot(BarsaTot_8['GolesVisitante'],kde=False, label='Barsa como visitante')
plt.title("2019-20 Madrid visitante vs Barsa visitante")
plt.legend()

#Histórico Madrid y Barcelona
#Temporada más anotadora vs peor Real Madrid
plt.figure(figsize = (20,10))
sns.distplot(Madrid_Tot_3['GolesLocal'],kde=False, label='Madrid en 14-15 ')
sns.distplot(Madrid_Tot_7['GolesLocal'],kde=False, label='Madrid en 18-19 ')
plt.title("Temporada más anotadora vs menos anotadora Real Madrid CF")
plt.legend()

plt.figure(figsize = (20,10))
sns.distplot(Madrid_Tot_3['GolesVisitante'],kde=False, label='Madrid en 14-15 ')
sns.distplot(Madrid_Tot_7['GolesVisitante'],kde=False, label='Madrid en 18-19 ')
plt.title("Temporada más anotadora vs menos anotadora Real Madrid CF")
plt.legend()

#Temporada más anotadora vs peor FC Barcelona
plt.figure(figsize = (20,10))
sns.distplot(BarsaTot_8['GolesLocal'],kde=False, label='FC Barcelona en 2019-20 ')
sns.distplot(BarsaTot_5['GolesLocal'],kde=False, label='FC Barcelona en 2016-17 ')
plt.title("Temporada más anotadora vs menos anotadora FC Barcelona local")
plt.legend()

plt.figure(figsize = (20,10))
sns.distplot(BarsaTot_8['GolesVisitante'],kde=False, label='FC Barcelona en 2019-20 ')
sns.distplot(BarsaTot_5['GolesVisitante'],kde=False, label='FC Barcelona en 2016-17 ')
plt.title("Temporada más anotadora vs menos anotadora FC Barcelona visitante")
plt.legend()

#Madrid vs Barcelona mejores temporadas:
plt.figure(figsize = (20,10))
sns.distplot(Madrid_Tot_3['GolesLocal'],kde=False, label='Madrid en 14-15 ')
sns.distplot(BarsaTot_5['GolesLocal'],kde=False, label='FC Barcelona en 2016-17 ')
plt.title("Temporada más anotadora Real Madrid vs temporada más  anotadora FC Barcelona local")
plt.legend()

plt.figure(figsize = (20,10))
sns.distplot(Madrid_Tot_3['GolesVisitante'],kde=False, label='Madrid en 14-15 ')
sns.distplot(BarsaTot_5['GolesVisitante'],kde=False, label='FC Barcelona en 2016-17 ')
plt.title("Temporada más anotadora Real Madrid vs temporada más  anotadora FC Barcelona visitantes")
plt.legend()





