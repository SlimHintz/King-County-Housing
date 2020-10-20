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