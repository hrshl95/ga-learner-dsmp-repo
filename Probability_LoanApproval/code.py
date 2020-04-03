# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# code starts here
df = pd.read_csv(path)
print(len(df))
p_a = df[df['fico'].astype(float)>700].shape[0]/df.shape[0]
print(p_a)
p_b = df[df['purpose']=='debt_consolidation'].shape[0]/df.shape[0]
print(p_b)
df1 = df[df['purpose']=='debt_consolidation']
print(df1)
p_a_b = df1[df1['fico'].astype(float)>700].shape[0]/ df1.shape[0]
print(p_a_b)
result=(p_a_b == p_a)
print(result)
# code ends here


# --------------
# code starts here
prob_lp = df[df['paid.back.loan']=='Yes'].shape[0] / df.shape[0]
print(prob_lp)
prob_cs = df[df['credit.policy']=='Yes'].shape[0] / df.shape[0]
print(prob_cs)
new_df = df[df['paid.back.loan']=='Yes']
print(new_df)
prob_pd_cs = new_df[new_df['credit.policy']=='Yes'].shape[0]/new_df.shape[0]
print(prob_pd_cs)
bayes = (prob_pd_cs*prob_lp)/prob_cs
print(bayes)
# code ends here


# --------------
# code starts here
df['purpose'].value_counts().plot(kind='bar')
plt.show()
df1 = df[df['paid.back.loan']=='No']
df1[df1['paid.back.loan']=='No'].plot(kind = 'bar')
plt.show()


# code ends here


# --------------
# code starts here

inst_median = df['installment'].median()
print(inst_median)
inst_mean = df['installment'].mean()
print(inst_mean)
plt.hist(df['installment'])
plt.show()
plt.hist(df['log.annual.inc'])
plt.show()



# code ends here


