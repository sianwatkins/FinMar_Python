import pandas as pd
import plotly.express as px
SP500 = pd.read_csv('C:\\Users\\siane\\OneDrive\\Documents\\FinMar_Python\\data_set\\SP500_data.csv')

print(SP500)

fig = px.bar(SP500, x="Date", y="SP500")
fig.show()