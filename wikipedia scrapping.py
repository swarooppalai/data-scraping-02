
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# Find all tables with class "wikitable sortable"
tables = soup.find_all('table', class_='wikitable sortable')

# Assuming you want to extract data from the first table, you can do the following:
table = tables[0]

#printing the desired table
print(table)

# Find all table header cells (th elements) within the table
headers = table.find_all('th')

# Extract the text content of each header cell
table_titles = [header.text.strip() for header in headers]

# Create an empty DataFrame with the extracted table titles as columns
df = pd.DataFrame(columns=table_titles)

# Print the DataFrame
#print(df)

df

row_data=table.find_all('td')


column_data= [titles.text.strip('\n') for titles in row_data]
#print(column_data)

sheet = [[] for _ in range(len(column_data)//7)]  # Create an empty list for each chunk


for i in range(len(column_data)//7):
    # Iterate within each chunk
    for j in range(7):
        index = i * 7 + j
        if index < len(column_data):
            sheet[i].append(column_data[index])


# Create a DataFrame directly from the sheet data
df = pd.DataFrame(sheet, columns=table_titles)

# Print the DataFrame
print(df)

df.to_csv(r'location\companies.csv',index=False)