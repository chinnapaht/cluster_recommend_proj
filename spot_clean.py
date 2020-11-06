import pandas as pd

def clean(df):
    df.drop('Unnamed: 0',axis = 1,inplace = True) #Drop the invalid Column

    df.drop_duplicates(subset ="title", 
                        keep = False, inplace = True) #Drop the duplicate song
        
    df["genre"].fillna("Unknown",inplace = True) #Fill the Nan value

    #Choose Only thai song
    rm_ind = list()
    for i in range(len(df)):
        gen = df.iloc[i]["genre"]
        if "thai"  not in gen.split() and 'Unknown'not in gen.split() :
            rm_ind.append(df.index[i])
    df_thai = df.drop(rm_ind)

    #Extract the feature added to be year and month
    df_thai['add_year'] = df_thai.added.str[:4]
    df_thai['add_month'] = df_thai.added.str[5:7]

    df_thai.drop("added",axis = 1,inplace = True     )
    return df_thai  