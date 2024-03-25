import pandas as pd

#loading the data
df=pd.read_excel('BCA_marks.xlsx')
df['total_avg']=(df['first_sem']+ df['second_sem']+df['third_sem']+ df['fourth_sem']+df['fifth_sem'])/5
df['credentials']=df['roll_no'].astype(str) +df['name'].apply(lambda x:' '+x)
df['first_sem_rank']=df['first_sem'].rank(ascending=False,method='dense').astype(int)
df['second_sem_rank']=df['second_sem'].rank(ascending=False,method='dense').astype(int)
df['third_sem_rank']=df['third_sem'].rank(ascending=False,method='dense').astype(int)
df['fourth_sem_rank']=df['fourth_sem'].rank(ascending=False,method='dense').astype(int)
df['fifth_sem_rank']=df['fifth_sem'].rank(ascending=False,method='dense').astype(int)
df['total_avg_rank']=df['total_avg'].rank(ascending=False,method='dense').astype(int)