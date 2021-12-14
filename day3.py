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
    
    return df.astype(int)

def day3(path):
    
    df = read_day3(path)
    
    gamma = df.mode()
    
    gamma['X'] = 'A'
    
    print(df.groupby('X').agg({
    'name': lambda x: ''.join(x)
}))
    


day3("aoc-input/day3_test_input.txt")