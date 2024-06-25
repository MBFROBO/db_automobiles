import pandas as pd

# from settings import SHEET_NAME



df = pd.ExcelFile('table.xlsx')
print(df.sheet_names)
