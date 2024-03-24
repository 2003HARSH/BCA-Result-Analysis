import pandas as pd

#loading the data
df=pd.read_excel('BCA_marks.xlsx')
df['total_avg']=(df['first_sem']+ df['second_sem']+df['third_sem']+ df['fourth_sem']+df['fifth_sem'])/5
df['credentials']=df['roll_no'].astype(str) +df['name'].apply(lambda x:' '+x)
