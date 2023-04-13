import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 784892881 # Ваш chat ID, не меняйте название переменной

def solution(x, y=None) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    
    if y==None:
        t_stat, p_val = ttest_ind(x, x)
    else:
        t_stat, p_val = ttest_ind(x, y)

    significance_level = 0.06
    
    if p_val < significance_level:
        return True         # print("Reject null hypothesis: there is a significant difference.")
    else:
        return False        # print("Fail to reject null hypothesis: there is no significant difference.")
