# Investigating the effect of explanatory variables on the SP500 index.
import pandas as pd
# import plotly.express as px
import statsmodels.formula.api as sm

from statsmodels.compat import lzip
import statsmodels.stats.api as sms

SP5002 = pd.read_csv('C:\\Users\\siane\\OneDrive\\Documents\\FinMar_Python\\data_set\\SP500_data.csv')


def regress_bp(SP5002):
    SP500 = SP5002["SP500"]
    dvnd = SP5002["Dividend"]
    erngs = SP5002["Earnings"]
    cpi = SP5002["Consumer Price Index"]
    lir = SP5002["Long Interest Rate"]
    rlprce = SP5002["Real Price"]
    rldvnd = SP5002["Real Dividend"]
    rlerngs = SP5002["Real Earnings"]
    pe10 = SP5002["PE10"]
    results = sm.ols(formula="SP500 ~ dvnd + erngs + cpi + lir + rlprce + rldvnd + rlerngs + pe10",
                     data=SP5002).fit()
    print(results.summary())
    return results


def breusch_pagan_test(results):
    #Breusch-Pagan test for Heteroscedasticity
    test = sms.het_breuschpagan(results.resid, results.model.exog)
    print("")
    names = ['Breusch Pagan Statistics', 'p-value',
             'f-value', 'f p-value']
    lzip(names, test)
    bp_results = pd.DataFrame([names, test])
    print(bp_results)
    return bp_results

def whites_test(results):
    #White's Test for Heteroscedasticity
    test = sms.het_white(results.resid, results.model.exog)
    names = ['White Statistic', 'p-value',
             'f-value', 'f p-value']
    lzip(names, test)
    white_results = pd.DataFrame([names, test])
    print(white_results)

reg = regress_bp(SP5002)
breusch_pagan_test(reg)
whites_test(reg)