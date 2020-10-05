"""
Piece Value Estimator

"""


__version__ = '0.1.1'


import pandas as pd
import sklearn.linear_model
import sklearn.metrics
from sklearn.model_selection import train_test_split


def main():   
    # (1) Prepare data
    csvfn = './data/chess_material.csv'
    df = pd.read_csv(csvfn)

    # Show in console.
    df.columns = ['epd', 'P-p', 'N-n', 'B-n', 'R-r', 'Q-q', 'result']
    print(df)

    # Redefine column names for regression.
    df.columns = ['epd', 'P', 'N', 'B', 'R', 'Q', 'result']
    
    total_row = df.shape[0]
    p_cnt = df[df['P'] > 0].shape[0]
    n_cnt = df[df['N'] > 0].shape[0]
    b_cnt = df[df['B'] > 0].shape[0]
    r_cnt = df[df['R'] > 0].shape[0]
    q_cnt = df[df['Q'] > 0].shape[0]
    
    print('\nFeatures that are not 0:')
    print('=======================\n')
    
    print(f'piece: P-p, num: {p_cnt}, pct: {100*p_cnt/total_row:0.2f}%')
    print(f'piece: N-n, num: {n_cnt}, pct: {100*n_cnt/total_row:0.2f}%')
    print(f'piece: B-b, num: {b_cnt}, pct: {100*b_cnt/total_row:0.2f}%')
    print(f'piece: R-r, num: {r_cnt}, pct: {100*r_cnt/total_row:0.2f}%')
    print(f'piece: Q-q, num: {q_cnt}, pct: {100*q_cnt/total_row:0.2f}%\n\n')

    # Don't include epd in the independent variable.
    X = df[['P', 'N', 'B', 'R', 'Q']]

    # Our target or objective value
    y = df['result']

    # Split data into training and test for validation.
    # 15% of the data is for testing.
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.15, random_state=1)
    
    # (2) Compare 4 models
    # Linear - https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html?highlight=regression#sklearn.linear_model.LinearRegression
    # Ridge - https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ridge_regression.html?highlight=ridge#sklearn.linear_model.ridge_regression
    # Lasso - https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html?highlight=lasso#sklearn.linear_model.Lasso
    # SGD - https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html?highlight=sgd#sklearn.linear_model.SGDRegressor
    models = dict()
    models.update({'Linear Regression': sklearn.linear_model.LinearRegression()})
    models.update({'Ridge': sklearn.linear_model.Ridge()})    
    models.update({'Lasso': sklearn.linear_model.Lasso(alpha=0.0001)})
    models.update({'Stochastic Gradient Descent': sklearn.linear_model.SGDRegressor()})
    
    # (3) Fit data   
    cnt = 0
    for k, model in models.items():
        model.fit(X_train, y_train)
        
        y_pred = model.predict(X_test)
        
        # Regression metrics
        mse = sklearn.metrics.mean_squared_error(y_test, y_pred)        
        mae = sklearn.metrics.mean_absolute_error(y_test, y_pred)
        r2_score = sklearn.metrics.r2_score(y_test, y_pred)
        
        print(f'model {cnt+1}: {k}')  
        print('=======================\n')
        
        print('Metrics:')
        print(f'mse: {mse}')
        print(f'mae: {mae}') 
        print(f'r2_score: {r2_score}\n')
        
        print(f'coefficients: {model.coef_}')            
        print(f'pawn: {model.coef_[0]*1000:0.0f},'
              f' knight: {model.coef_[1]*1000:0.0f},'
              f' bishop: {model.coef_[2]*1000:0.0f},'
              f' rook: {model.coef_[3]*1000:0.0f},'
              f' queen: {model.coef_[4]*1000:0.0f}\n\n')
        
        cnt += 1

    print('References:')
    print('mse      : mean squared error')
    print('mae      : mean absolute error')
    print('r2_score : coefficient of determination')


if __name__ == '__main__':
    main()
