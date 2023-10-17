import pandas as pd
import matplotlib.pyplot as plt

# read the CSV file into a DataFrame
df = pd.read_csv('norway_municipalities_2017.csv')

# group by 'District' and sum the 'Population'
grouped = df.groupby('District').Population.sum().sort_values(ascending=False)

# plot the data
grouped.plot(kind='bar')
plt.ylabel('Population')
plt.title('Population of Norwegian Districts (2017)')
plt.tight_layout()

plt.show()
