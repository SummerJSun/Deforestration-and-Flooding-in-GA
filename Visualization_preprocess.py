import os
import pandas as pd
import glob

#1.read in and combine all the datasets

csv_files = glob.glob("*.csv")

df_list = []

for file in csv_files:
    name = os.path.splitext(os.path.basename(file))[0]
    df = pd.read_csv(file)
    df = df.iloc[:,:-1]
    
    df_melted = pd.melt(
        df,
        id_vars=['Period'],
        var_name='Year',
        value_name='Area'
    )


    df_melted['County']=name

    df_list.append(df_melted)

combined_df = pd.concat(df_list,ignore_index=True)
combined_df['Year'] = combined_df['Year'].str[:4]

Combined_NLCD = pd.DataFrame(combined_df) 
Combined_NLCD.to_csv(os.path.join("./Processed", "Combined_NLCD.csv"))




