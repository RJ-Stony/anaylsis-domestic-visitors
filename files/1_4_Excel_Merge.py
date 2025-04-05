import pandas as pd

excel_names = ['./files/melon.xlsx',
               './files/bugs.xlsx',
               './files/genie.xlsx']

merged_data = pd.DataFrame()

for name in excel_names:
    df = pd.read_excel(name)
    merged_data = pd.concat([merged_data, df], ignore_index=True)
    
merged_data.info()
merged_data.to_excel('./files/total.xlsx', index=False)
