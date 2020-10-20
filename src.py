def geo_hash(lat, long, n_chars=5):
    """
    A geohashing function to apply to a dataframe
    """
    return geohash2.encode(lat, long, 5)

def get_interactions(df, choose=2):
    """
    df --> pd.seriesdataframe
    returns --> pd.dataframe
    
    Given a dataframe, this function takes all of the columns and generates an a new column based on their
    multiplicative interaction.
    
    dependent on itertools and pandas
    """
    columns = itertools.permutations(df.columns,choose)
    interaction = {' X '.join(x): df[x[0]]*df[x[0]] for x in columns}
    return pd.DataFrame.from_dict(interaction)

def multicolinear_features(data):
    """
    Given a data frame of features, this function returns a list of features that are colinear
    """
    df=data.corr().abs().stack().reset_index().sort_values(0, ascending=False)
    df['pairs'] = list(zip(df.level_0, df.level_1))
    df.set_index(['pairs'], inplace = True)
    df.drop(columns=['level_1', 'level_0'], inplace = True)
    df.columns = ['cc']
    return df[(df.cc>.75) & (df.cc <1)]