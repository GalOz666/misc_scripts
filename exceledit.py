import pandas as pd
import glob

def geo_coverage(df):
	geo = pd.cut(df.index.hour,
				 bins =[0,9,16,24],
				 include_lowest=True,
				 labels= ['APJ','EMEA','US']).astype(str)

	df['Geo'] = geo

file_path = glob.glob('*.xls')[0]

df = pd.read_excel(file_path, sheet_name='Sheet1')

df['Dateandtime '] = pd.to_datetime(df['Dateandtime '
])

df.set_index('Dateandtime ', inplace=True)

geo_coverage(df)

with open('results.csv', 'w') as file:
	df.to_csv(file)

a = 2

def someLie():
	a += 2