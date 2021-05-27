import pandas as pd
import plotly.express as px
import statsmodels.formula.api as sm
from statsmodels.compat import lzip
import statsmodels.stats.api as sms
import numpy as np

SP5002 = pd.read_csv('C:\\Users\\siane\\OneDrive\\Documents\\FinMar_Python\\data_set\\SP500_data.csv')

# log the SP500 for readings in % change
lnSP500 = SP5002["SP500"].apply(np.log)
# add new variable to the dataframe
SP5002['lnSP500'] = lnSP500
# selecting explanatory variables
dvnd = SP5002["Dividend"]
erngs = SP5002["Earnings"]
cpi = SP5002["Consumer Price Index"]
lir = SP5002["Long Interest Rate"]
rlprce = SP5002["Real Price"]
rldvnd = SP5002["Real Dividend"]
rlerngs = SP5002["Real Earnings"]
pe10 = SP5002["PE10"]


def describe_data(SP5002):
    index = SP5002["SP500"]
    include = ['object', 'float', 'int']
    desc = index.describe(include=include)
    print(desc)
    print(SP5002.info())
    print(SP5002['Consumer Price Index'].describe())


def regress_bp(SP5002):
    results = sm.ols(formula="lnSP500 ~ dvnd + erngs + cpi + lir + rlprce + rldvnd + rlerngs + pe10",
                     data=SP5002).fit()
    print(results.summary())
    return results


def breusch_pagan_test(results):
    # Breusch-Pagan test for Heteroscedasticity
    test = sms.het_breuschpagan(results.resid, results.model.exog)
    print("")
    names = ['Breusch Pagan Statistics', 'p-value',
             'f-value', 'f p-value']
    lzip(names, test)
    bp_results = pd.DataFrame([names, test])
    print(bp_results)
    return bp_results


def whites_test(results):
    # White's Test for Heteroscedasticity
    test = sms.het_white(results.resid, results.model.exog)
    names = ['White Statistic', 'p-value',
             'f-value', 'f p-value']
    lzip(names, test)
    white_results = pd.DataFrame([names, test])
    print(white_results)


def robust_se_OLS(SP5002):
    robust = sm.ols(formula="SP500 ~ dvnd + erngs + cpi + lir + rlprce + rldvnd + rlerngs + pe10",
                    data=SP5002).fit(cov_type='HC1')
    print(robust.summary())
    hypotheses = '(dvnd =0), (cpi =0)'
    f_test = robust.f_test(hypotheses)
    print("")
    print("F TEST")
    print(f_test)
    print("SSR")
    print(robust.ssr)
    return robust

def plot(SP5002):
    fig = px.line(SP5002, x="Real Dividend", y="lnSP500", title='Dividends on ln(SP500)')
    fig.show()

describe_data(SP5002)
reg = regress_bp(SP5002)
breusch_pagan_test(reg)
whites_test(reg)
rbst = robust_se_OLS(SP5002)
plot(SP5002)
