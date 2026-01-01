#create a new dataframe
import pandas as pd

df = pd.DataFrame(
    {
        'name': ['john','marc','elizabeth'],
        'age': [18,23,34],
        'steps': [10000,12343,15665]
    }
)

print(df)

#select only steps column
steps_df = df[['steps']]
ages_df = df[['age']]
#steps_df is a copy or a reference? answer: copy
print(steps_df)
print(ages_df)
#What if I want to just reference? Use .loc or .iloc
steps_ref = df.loc[:,['steps']]
print(df.loc[:,['steps']])

#modify the age of the first person
df.loc[0,'age'] = 20
print(df.loc[:, :])

print(df[["name"]])

#add a new column calories
df['calories'] = [544, 443, 665]

print(df)

#select calories and steps and compute a new column: calories per step
df['cal_per_step'] = df['calories'] / df['steps']
print(df.loc[:, 'cal_per_step'])
print(df)

#rename: steps to daily_steps
df.rename(columns={'steps':'asdasd'}, inplace=True)
#what does inplace is for? answer: It modifies the original dataframe instead of returning a new one.
print(df)  
#round to 3 decimals cal per step:
df['cal_per_step'] = df['cal_per_step'].round(3)
print(df)