# Piece Value Estimator
Estimates the piece value coefficient by different linear regression models given a data of chess piece values with results.

### Setup
* Install python
* Install sklearn
  * pip install sklearn
* Install pandas
  * pip install pandas
  
### Regression models
* [Linear](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html?highlight=regression#sklearn.linear_model.LinearRegression)
* [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ridge_regression.html?highlight=ridge#sklearn.linear_model.ridge_regression)
* [Lasso](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html?highlight=lasso#sklearn.linear_model.Lasso)
* [Stochastic Gradient Descent](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html?highlight=sgd#sklearn.linear_model.SGDRegressor)

### Sample output
```
                                                       fen  P-p  ...  Q-q  result
0        r3r3/pbp1kp2/2p2bpp/2N1p3/8/5B2/PPP2PPP/2KRR3 ...   -1  ...    0       1
1        3rr1k1/pb4pp/2p1n3/1p1n4/1P1qN3/P7/B1Q2PPP/3R1...    0  ...    0       0
2          6k1/p1p3p1/1p5p/4p3/2P2n2/2P2B2/P4P1P/6K1 w - -   -1  ...    0       0
3              6k1/6p1/2p5/p1q4p/2P1n3/p4RNP/R5P1/7K b - -   -2  ...   -1       0
4          4rk2/1R5p/6p1/r2P1p2/p1PpB3/5P2/P5PP/4K2R w K -    1  ...    0       1
...                                                    ...  ...  ...  ...     ...
1206278                 8/pp6/2pk4/5R2/1P6/r7/5PK1/8 w - -   -1  ...    0       0
1206279                      1r6/8/8/8/R6p/6nk/5K2/8 w - -   -1  ...    0       0
1206280                    7R/6p1/6k1/4Kp2/6rP/8/8/8 w - -   -1  ...    0       0
1206281    1r2k3/1q3p1p/p3pQ2/8/2pR4/5Pr1/1PP3P1/R6K b - -   -1  ...    0       1
1206282                 8/8/8/4p1p1/1K1kP1P1/5P2/8/8 b - -    1  ...    0       0

[1206283 rows x 7 columns]

Features that are not 0:
=======================

piece: P-p, num: 579322, pct: 48.03%
piece: N-n, num: 254340, pct: 21.08%
piece: B-b, num: 251468, pct: 20.85%
piece: R-r, num: 117705, pct: 9.76%
piece: Q-q, num: 24378, pct: 2.02%


model 1: Linear Regression
=======================

Metrics:
mse: 0.16410313874489252
mae: 0.3518987466042799
r2_score: 0.3396676182349635

coefficients: [0.17450496 0.33598911 0.37350445 0.52490821 0.96500647]
pawn: 175, knight: 336, bishop: 374, rook: 525, queen: 965


model 2: Ridge
=======================

Metrics:
mse: 0.16410313539039326
mae: 0.35189949045291846
r2_score: 0.33966763173308734

coefficients: [0.1745041  0.33597642 0.37349147 0.5248878  0.96495136]
pawn: 175, knight: 336, bishop: 373, rook: 525, queen: 965


model 3: Lasso
=======================

Metrics:
mse: 0.16410447794342517
mae: 0.35203124553077647
r2_score: 0.33966222945225355

coefficients: [0.17432736 0.33381853 0.37129856 0.52166285 0.95753882]
pawn: 174, knight: 334, bishop: 371, rook: 522, queen: 958


model 4: Stochastic Gradient Descent
=======================

Metrics:
mse: 0.16415350143193788
mae: 0.35034513471558837
r2_score: 0.3394649645054669

coefficients: [0.17870765 0.33873901 0.37098609 0.53000329 0.96326733]
pawn: 179, knight: 339, bishop: 371, rook: 530, queen: 963


References:
mse      : mean squared error
mae      : mean absolute error
r2_score : coefficient of determination
```

### Credits
* [A post from talkchess](http://talkchess.com/forum3/viewtopic.php?f=7&t=75267)
* [RBloggers](https://www.r-bloggers.com/2015/06/big-data-and-chess-what-are-the-predictive-point-values-of-chess-pieces/)
* [The Week In Chess](https://theweekinchess.com/)
