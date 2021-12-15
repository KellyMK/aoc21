import pandas as pd

def read_day3(path):
    
    # Read in data from file path
    df = pd.read_table(path, sep=' ', header=None, dtype='str')
    df = df[0].str.split('',n=500,expand=True)

    # Define float NaN to remove empty strings
    nan_value = float("NaN")
    # Replace all empty strings with NaN
    df.replace("", nan_value, inplace=True)
    # Remove all NaN values 
    df.dropna(how='all', axis=1, inplace=True)
    
    return df

def least_common(x, rank=-1):
    """[summary]

    Args:
        x (data frame column): input DF column
        rank (int, optional): Rank, where 0 = most frequent, -1 = least frequent, 
        and other integers represent the rank. Defaults to -1.
    """
    
    cnts = x.value_counts()
    
    return cnts.index[rank]
    
    

def calc_nums(df):
    
    print('df')
    print(df)
    
    gamma = ''.join(df.mode().values.tolist()[0])
    gamma_int = int(gamma)
    gamma_dec = int(gamma, base=2)
    
    print(gamma_int)
    print(gamma_dec)
    
    epsilon = ''.join(df.agg([least_common]).values.tolist()[0])
    epsilon_int = int(epsilon)
    epsilon_dec = int(epsilon, base=2)
    
    print(epsilon_int)
    print(epsilon_dec)
    
    return gamma_dec * epsilon_dec


def day3a(path):
    df = read_day3(path)
    
    return calc_nums(df)


day3a("test/day3_test_input.txt")