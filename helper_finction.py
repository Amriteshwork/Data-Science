### Count the number of unique words in the dataframe saperated by ","

import pandas as pd

def clean_dataframe(df):
    df = df[["predictions"]]
    pattern =  r'[\[\]\'\"]'
    for col in df.columns:
        df[col] = df[col].apply(lambda x: re.sub(pattern, '', str(x)))
        
    return df

def count_words_in_column(column):
    words = column.str.split(', ')
    unique_words = set(word for row in words for word in row)
    word_counts = {word: sum(row.count(word) for row in words) for word in unique_words}
    df_word_counts = pd.DataFrame(word_counts.items(), columns=['word', 'count'])

    return df_word_counts
  
  ################################################################################################################
