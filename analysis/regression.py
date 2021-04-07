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
    BetaHAT2 = SP5002["Long Interest Rate"]
    d = {"Y": pd.Series(Y), "BetaHAT1": pd.Series(BetaHAT1), "BetaHAT2": pd.Series(BetaHAT2)}
    df = pd.DataFrame(d)
    result = sm.ols(formula="Y ~ BetaHAT1 + BetaHAT2", data=df).fit()
    sian = result.summary()
    print(sian)
    return sian


# def interpret(sian):
# print("Hypothesis Test for the Significance of B")
# print(sian)


lobf(SP5002)
reg = regress(SP5002)
# interpret(reg)

##############Check if something is a dataframe (HELPFUL)
# if isinstance(sian, pd.DataFrame):
#   print("YESSSSS")
