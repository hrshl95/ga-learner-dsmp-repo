# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#path of the data file- path
data = pd.read_csv(path)
print(data.head(2))
data['Gender'].replace('-','Agender', inplace = True)
# print(data['Gender'])
#Code starts here 
gender_count = data['Gender'].value_counts()
print(gender_count)
gender_count.plot(kind='bar')
plt.show()



# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
plt.pie(alignment, labels=alignment.index, autopct='%1.1f %%')
plt.title('Character Alignment')
plt.show()


# --------------
#Code starts here
sc_df = data[['Strength','Combat']]
print(sc_df.head(3))
sc_covariance = sc_df.cov().iloc[0,1]
print(sc_covariance)
sc_strength = sc_df['Strength'].std()
print(sc_strength)
sc_combat = sc_df['Combat'].std()
print(sc_combat)
sc_pearson = sc_covariance / (sc_strength * sc_combat)
print(sc_pearson)
ic_df = data[['Intelligence', 'Combat']]
ic_covariance = ic_df.cov().iloc[0,1]
print(ic_covariance)
ic_intelligence = ic_df['Intelligence'].std()
print(ic_intelligence)
ic_combat = ic_df['Combat'].std()
print(ic_combat)
ic_pearson = ic_covariance / (ic_intelligence * ic_combat)
print(ic_pearson)


# --------------
#Code starts here
total_high = data['Total'].quantile(q=0.99)
print(total_high)
super_best = data[data['Total']>total_high]
# print(super_best)
super_best_names = [['Name', super_best]]
print(super_best_names)


# --------------
#Code starts here

fig ,(ax_1, ax_2, ax_3) = plt.subplots(nrows=3,ncols=1, figsize=(20,10)) 
ax_1.boxplot(data['Intelligence'])
ax_1.set_title('Intelligence')
ax_2.boxplot(data['Speed'])
ax_2.set_title('Speed')
ax_3.boxplot(data['Power'])
ax_3.set_title('Power')
plt.show()


