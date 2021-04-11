import pandas as pd
import plotly.express as px
import statsmodels.formula.api as sm

SP5002 = pd.read_csv('C:\\Users\\siane\\OneDrive\\Documents\\FinMar_Python\\data_set\\SP500_data.csv')


def lobf(SP5002):
    # effect of dividend on the SP500 index
    graph2 = px.scatter(SP5002, x='Dividend', y='SP500', trendline='ols')
    graph2.show()
    return graph2


def regress(SP5002):
    Y = SP5002["SP500"]
    BetaHAT1 = SP5002["Dividend"]
    BetaHAT2 = SP5002["Earnings"]
    BetaHAT3 = SP5002["Consumer Price Index"]
    BetaHAT4 = SP5002["Long Interest Rate"]
    results = sm.ols(formula="Y ~ BetaHAT1 + BetaHAT2 + BetaHAT3 + BetaHAT4", data=SP5002).fit()
    # print(results.summary())
    return results


def important_values(results):
    r2 = results.rsquared
    f = results.fvalue
    ssr = results.ssr
    important_reg_output = pd.DataFrame([[r2, f, ssr]], columns=['R-Squared', 'F-Statistic', 'SSR'])
    print(important_reg_output)
    return important_reg_output


lobf(SP5002)
reg = regress(SP5002)
useful_df = important_values(reg)
