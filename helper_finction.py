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


#######################################################################################################################################

## Download CSV data from GitHub
import requests
from io import StringIO

url = "https://raw.githubusercontent.com/dr5hn/countries-states-cities-database/master/csv/cities.csv"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0"}
req = requests.get(url, headers=headers)
data = StringIO(req.text)

dataframe = pd.read_csv(data)


##########################################################################################################################################

## Delete the column from the subfolder with column name specified

def delete_columns(folder_path):
    # loop through all files and subfolders recursively
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith('.csv'):
                # read the csv file into a pandas dataframe
                df = pd.read_csv(os.path.join(root, filename))
                # keep only the first and third column, and rename them
                df = df.iloc[:, [0, 2]]
                df = df.rename(columns={df.columns[0]: 'district', df.columns[1]: 'city'})
                # add a new column "state" and populate it with the subfolder name
                state = os.path.basename(root)
                df['state'] = state
                # save the updated dataframe as a new csv file with '_updated' suffix
                new_filename = os.path.splitext(filename)[0] + '_updated.csv'
                new_path = os.path.join(root, new_filename)
                df.to_csv(new_path, index=False)
                
                
                
################################################################################################################################################

## combine different csv file present in sub-folder

import os
import pandas as pd

def combine_csv_files(parent_folder, output_file):
    # create an empty list to store dataframes
    dfs = []

    # loop through each subfolder in the parent folder
    for subfolder in os.listdir(parent_folder):
        # check if the current item is a folder
        if os.path.isdir(os.path.join(parent_folder, subfolder)):
            # get a list of all files in the subfolder
            file_list = os.listdir(os.path.join(parent_folder, subfolder))

            # filter the list to only include files ending in "_updated.csv"
            file_list = [f for f in file_list if f.endswith("_updated.csv")]

            # loop through each file, read it into a dataframe, and append it to the list of dataframes
            for file in file_list:
                df = pd.read_csv(os.path.join(parent_folder, subfolder, file))
                dfs.append(df)

    # concatenate all dataframes in the list into a single dataframe
    combined_df = pd.concat(dfs, ignore_index=True)

    # write the combined dataframe to a new csv file
    combined_df.to_csv(output_file, index=False)

    return combined_df

