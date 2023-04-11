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

## Scrap the data when the data is in JSON format in HTML page.

import requests
import json
import csv

url = 'https://newsdata.io/api/1/archive?apikey=pub_xxxxx&q=news'

# get all data
all_data = []

while url:
    response = requests.get(url)
  
########################################################################################################################

## print the no. of arg. in simple transformer lib
arg_values = []

pd.set_option('display.max_rows', 80)

# For all of the arguments...
for arg in dir(model.args):
    
    # Skip over the special attributes and any functions.
    if (not arg[0:2] == '__') and (not callable(getattr(model.args, arg))):
    
        # Store the argument and its value as a tuple.
        arg_values.append((arg, str(getattr(model.args, arg))))

# Store as a dataframe just to get the pretty printout.
df_args = pd.DataFrame(arg_values)        

df_args

    try:
        data = json.loads(response.content)
    except json.JSONDecodeError:
        print("Error: Invalid JSON")
        break
    else:
        for item in data['results']:
            all_data.append(item)

        if data['nextPage']:
            url = f"{url}&page={data['nextPage']}"
            print(url)
        else:
            url = None

if all_data:
    keys = all_data[0].keys()

    with open("data_given/content_1.csv", "w", newline='') as f:  # 9211    #	1598789
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for item in all_data:
            writer.writerow(item)
else:
    print("Error: No data retrieved")
    
    
    
    
    
    
 ########################################################################################################################

## Print the argument of the model can use 
## works for Simple Transformer lib

arg_values = []

pd.set_option('display.max_rows', 80)

# For all of the arguments...
for arg in dir(model.args):
    
    # Skip over the special attributes and any functions.
    if (not arg[0:2] == '__') and (not callable(getattr(model.args, arg))):
    
        # Store the argument and its value as a tuple.
        arg_values.append((arg, str(getattr(model.args, arg))))

# Store as a dataframe just to get the pretty printout.
df_args = pd.DataFrame(arg_values)        

df_args
