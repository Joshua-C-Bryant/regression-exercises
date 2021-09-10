import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.metrics import mean_squared_error, r2_score

from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import f_regression 
from math import sqrt
import seaborn as sns

def plot_residuals(x,y,yhat):
    residual = y - yhat
    plt.scatter(x, residual)
    plt.axhline(y = 0, ls = ':')
    plt.xlabel('x')
    plt.ylabel('Residual')
    plt.title('OLS model residuals');   

def regression_errors(y, yhat):
    residual = y - yhat
    SSE = (residual**2).sum()
    ESS = sum((yhat - y.mean())**2)
    TSS = ESS + SSE
    MSE = SSE/len(y)
    RMSE = sqrt(MSE)
    print('SSE =','{:.2f}'.format(SSE))
    print('ESS =','{:.2f}'.format(ESS))
    print('TSS =','{:.2f}'.format(TSS))
    print('MSE =','{:.2f}'.format(MSE))
    print('RMSE =','{:.2f}'.format(RMSE))

def baseline_mean_errors(y):
    baseline = y.mean()
    baseline_residual = y - baseline
    SSE_baseline = (baseline_residual**2).sum()
    MSE_baseline = (SSE_baseline/len(y))
    RMSE_baseline = sqrt(MSE_baseline)
    print('SSE_baseline =','{:.2f}'.format(SSE_baseline))
    print('MSE_baseline =','{:.2f}'.format(MSE_baseline))
    print('RMSE_baseline =','{:.2f}'.format(RMSE_baseline))

def better_than_baseline(y,yhat):
    residual = y - yhat
    SSE = (residual**2).sum()
    baseline = y.mean()
    baseline_residual = y - baseline
    SSE_baseline = (baseline_residual**2).sum()
    return SSE < SSE_baseline