import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

data_FULL = pd.read_csv("TRAINING_DATA.txt")
data_FULL = data_FULL.drop_duplicates()


Y_FULL = data_FULL["so2"]
X_FULL = data_FULL.drop(["so2"], axis = 1)


Y_train = Y_FULL[:-20]
Y_test  = Y_FULL[-20:]

X_train = X_FULL[:-20]
X_test  = X_FULL[-20:]






regr1 = linear_model.LinearRegression()
regr1.fit(X_train, Y_train)
#print(regr1.coef_)
#print(regr1.intercept_)

def multi_lin_reg(X_tr, X_te, Y_tr, Y_te):
    """
    Inputs: 
        - X_tr = predictor training data
        - X_te = predictor test data
        - Y_tr = response training data
        - Y_te = response test data
        
    Outputs:
        - Dictionary of values, from the LinReg model.
        
        
    f(x)
        - Give it a list of train and test data, and it will fit a
            Linear Regression model on the data, and test the model,
            and give you some useful statistic.
        
    """
    # fits regression model to Training Data (X_tr, Y_tr)
    regr = linear_model.LinearRegression()
    regr.fit(X_tr, Y_tr)
    
    # makes predictions for Y, using Test Data (X_te)
    Y_pred = regr.predict(X_te)
    
    model_results = {}
    model_results['X_variables'] = X_tr.columns.values.tolist()
    model_results['Coefficients'] = regr.coef_
    model_results['MeanSqError'] = mean_squared_error(Y_te, Y_pred)
    model_results['R2_Score'] = r2_score(Y_te, Y_pred)
    #model_results['Y_predicted'] = Y_pred #comment this line out later
    #model_results['Y_test'] = Y_te #comment this line out later
    model_results['Ytest_vs_Ypred'] = list(zip(Y_te, Y_pred))
    return model_results


#print(Y_FULL.head(10))
#print(X_FULL.head(10))
ccc= multi_lin_reg(X_train, X_test, Y_train, Y_test)
print(ccc['R2_Score'])
print(ccc['MeanSqError'])
print(ccc['X_variables'])






#print(bin(2)[2:].zfill(8))

def generate_bin_strings(N):
    """
    Generates all possible binary strings, up to length N.
    Use for the permutations of possible model predictors
    """
    total = 2**N
    bin_strings = []
    for i in range(0, total):
        bin_str = bin(i)[2:].zfill(N)
        bin_strings.append(bin_str)
    #print("Total = " + str(total))
    return bin_strings   
    
zzzz = generate_bin_strings(4)


def binary_locate_in_df(dataframe ,binarystring):
    """
    Wherever there's a 0 in the binary string,
    it removes the corresponding column from the dataframe.
    """
    temp_df = dataframe
    remove_list = []
    for i in range(0, len(binarystring)):
        print(i, int(binarystring[i]), temp_df.columns[i])
        #print(binarystring[i])
        #print(temp_df.columns[i])
        if int(binarystring[i]) == 0:
            remove_list.append(int(i))
    
    temp_df = temp_df.drop(temp_df.columns[remove_list], axis = 1)      
   
    return temp_df

ooooo = binary_locate_in_df(data_FULL, "11001101")
# so for this one, wind.velocity, wind.direction and temperature.1 should be removed...
# YEPPP WORKS SO FAR...
