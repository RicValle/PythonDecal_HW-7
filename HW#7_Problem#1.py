
import pandas as pd 

file = "AOC_recent_tweets.txt"

df = pd.read_json(file)

def time_in_hours(datatime_column):

    return datatime_column.dt.hour + (datatime_column.dt.minute / 60) + (datatime_column.dt.second / (60 ** 2))

df['created_at'] = pd.to_datetime(df['created_at'])
df['hours'] = time_in_hours(df['created_at'])

df_selected = df[['created_at', 'hours', 'full_text']]
                                                                         
New_File = 'C:/Users/rvall/PYDECAL/AOC_tweets_with_hours.csv'
df_selected.to_csv(New_File, index = False)
print("CSV file saved succesfully") 