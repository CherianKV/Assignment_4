def maybe_yes_no_to_num(df2, clm_name):
    df2.loc[(df2[clm_name].isin(['Yes', 'Maybe'])), clm_name] = 1
    df2.loc[(df2[clm_name].isin(['No','Some of them'])), clm_name] = 0


def dnt_know_no_yes_to_num(df2, clm_name):
    df2.loc[(df2[clm_name].isin(["No", "Not sure", "Don't know"])), clm_name] = 0
    df2.loc[(df2[clm_name].isin(["Yes"])), clm_name] = 1