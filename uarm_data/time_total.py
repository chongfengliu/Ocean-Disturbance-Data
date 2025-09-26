import pandas as pd
import os

folder_path = './'

total_difference = 0
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)

        df = pd.read_csv(file_path)

        first_value = df.iloc[0, 1]
        last_value = df.iloc[-1, 1]

        difference = last_value - first_value

        total_difference += difference

        print(f"The difference for {filename} is: {difference}")

        total_time = total_difference / (1000 * 60 * 60)
        print(f"The total time is: {total_time} hrs.")