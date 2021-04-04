import pandas as pd
import plotly.express as px
import statsmodels.formula.api as sm

SP5002 = pd.read_csv('C:\\Users\\siane\\OneDrive\\Documents\\FinMar_Python\\data_set\\SP500_data.csv')


def lobf():
    # effect of dividend on the SP500 index
    graph2 = px.scatter(SP5002, x='Dividend', y='SP500', trendline='ols')
    graph2.show()
    return graph2


scattergraph = lobf()
A = SP5002["SP500"]
B = SP5002["Dividend"]
C = SP5002["Long Interest Rate"]
result = sm.ols(formula="A ~ B + C", data=SP5002).fit()
print(result.params)
print(result.summary())
