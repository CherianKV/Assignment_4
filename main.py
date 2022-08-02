import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from cleaning_functions import maybe_yes_no_to_num
from cleaning_functions import dnt_know_no_yes_to_num

# %matplotlib inline

pd.set_option('display.max_columns', 50)

# Load Dataset
df = pd.read_csv('./survey.csv')
# print(df.head())

to_drop = ['comments', 'Timestamp', 'no_employees']
df = df.drop(to_drop, axis=1)
l_maybe_no_yes = ["coworkers", "supervisor", "self_employed", "family_history", "remote_work", "obs_consequence",
                  "treatment", "mental_health_consequence", "phys_health_consequence", "phys_health_interview",
                  "mental_health_interview"]

l_dntknow_yes_no = ['benefits', 'care_options', 'wellness_program', 'seek_help'
    , 'anonymity', 'mental_vs_physical']
df.loc[(df['self_employed'].isna()), 'self_employed'] = 'No'

for i in l_maybe_no_yes:
    print(i)
    maybe_yes_no_to_num(df, i)

for i in l_dntknow_yes_no:
    print(i)
    dnt_know_no_yes_to_num(df, i)

df.loc[(df['Gender'].isin(['M', 'Male', 'male', 'm', 'Male-ish', 'maile'
                              , 'something kinda male?', 'Cis Male', 'Mal', 'Male (CIS)'
                              , 'Make', 'Guy (-ish) ^_^', 'male leaning androgynous', 'Male '
                              , 'Man', 'msle', 'Mail', 'cis male', 'Malr', 'Cis Man'
                              , 'ostensibly male, unsure what that really means'])), 'Gender'] = 'Male'

df.loc[(df['Gender'].isin(['Female', 'female', 'Cis Female', 'F', 'Woman', 'f'
                              , 'queer/she/they', 'Femake', 'woman', 'Female '
                              , 'cis-female/femme', 'Female (cis)', 'cis male'
                              , 'femail'])), 'Gender'] = 'Female'

df.loc[(df['Gender'].isin(['Trans-female', 'non-binary', 'Nah', 'All', 'Enby'
                              , 'fluid', 'Genderqueer', 'Androgyne', 'Agender'
                              , 'Trans woman', 'Neuter', 'Female (trans)', 'queer'
                              , 'A little about you', 'p'])), 'Gender'] = 'Non-Binary'

df.loc[(df['state'].isna()), 'state'] = 'Non US State'

df.loc[(df['work_interfere'].isna()), 'work_interfere'] = 'Sometimes'

df.loc[(df['leave'].isin(["Don't know"])), 'leave'] = 'Somewhat difficult'


df.loc[(df['Age'].isin(range(0, 19))), 'Age_Grp'] = 'Kids & Teens'
df.loc[(df['Age'].isin(range(19, 30))), 'Age_Grp'] = "Young Adults"
df.loc[(df['Age'].isin(range(30, 50))), 'Age_Grp'] = 'Middle Aged'
df.loc[(df['Age'].isin(range(50, 100))), 'Age_Grp'] = 'Seniors'
df.loc[(~df['Age'].isin(range(0, 100))), 'Age_Grp'] = np.nan

for i in df.columns:
    print(i)
    print(df[i].unique())

# print(len(df))

df = df.dropna()



f1=plt.figure(1)
dfg = df.groupby(['Country'])['treatment'].sum()
plt.title('Number of people who had treatment for mental health issues')
dfg.plot(kind='bar')


f2 = plt.figure(2)

dfg = df.groupby(['Country'])['family_history'].sum()
plt.title('Number of people who had a family member with history of mental health issues')
dfg.plot(kind='bar')


f3 = plt.figure(3)

dfg = df.groupby(['Country'])['obs_consequence'].sum()
plt.title('Number of people who had  '
          'observed negative consequences for coworkers with mental health conditions in their workplace')
dfg.plot(kind='bar')

f4 = plt.figure(4)

dfg = df.groupby(['Country'])['coworkers'].sum()
plt.title('Number of people who can talk to coworkers about their mental health issues')
dfg.plot(kind='bar')

f5 = plt.figure(5)

dfg = df.groupby(['Country'])['wellness_program'].sum()
plt.title('Number of people who have Wellness Programmes in their workplace')
dfg.plot(kind='bar')

f6 = plt.figure(6)

dfg = df.groupby(['Country'])['seek_help'].sum()
plt.title("Number of people who's employer provide resources to "
          "learn more about mental health issues and how to seek help?")
dfg.plot(kind='bar')


f7 = plt.figure(7)

dfg = df.groupby(['Country'])['benefits'].sum()
plt.title("Number of people who's employer provide mental health benefits")
dfg.plot(kind='bar')

f7 = plt.figure(8)

dfg = df.groupby(['Country'])['supervisor'].sum()
plt.title("Number of people who can talk to their supervisor about mental health issues")
dfg.plot(kind='bar')

plt.show()

input()
