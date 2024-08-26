# Goalscorer confidence

Does confidence matter for converting chances into goals in football? Can machine learning help?

xG is a popular metric in football analysis. It measures how likely it is that a specific shot results in a goal. However, mental factors are rarely taken into account. Therefore, a new metric - **AwareXG** - was devised in this analysis, to investigate how pressure and self-belief impact chance conversion.

The analysis is done using Pandas and sklearn. Understat's xG model and shot data is used, while betting data is scraped from OddsPortal.

Keywords: machine learning, statistical analysis, web scraping, pandas, sports, football

## Introduction

xG is calculated from the location of the shot-taker, the goalkeeper's position, the speed of the ball, and other physical features, and mathematically it is the expected value of the number of goals scored from the shot-taking situation. 

**Popular classification models are of no use in this problem.** Most xG values are under 0.3, so any combination of positive mental attributes is still unlikely to result in a goal, because of the paucity of high-xG chances. Accurate prediction is impossible here, and it is what most ML models are made to do. Additionally, xG is already present in the data, which should be used since it already gives a great estimate for the chance that a goal will be scored.

The problem can be stated as improvement of an expected value estimate, taking further variables (mental factors) into account.

## Methods

At first, I wanted to see if scoring a goal earlier in the match meant that a player would score more efficiently. I counted the total xG and total goals after already scoring a goal - however, I got the contrary result. I realized that other correlated variables were probably at fault. Therefore, I needed to do proper feature extraction with an ML model.

The statistical model used is described by the equation:

$$ \text{AwareXG} = \text{xG} * (1 + \beta + \sum_{i}^{} \alpha_{i} x_i) $$

where $x_i$ are the features, and $\alpha_{i}$ and $\beta$ are the model parameters. This works because no mental factors were ever observed which are better predictors than xG, so any real formula can be well approximated by this model.

With careful feature engineering (to get linear relationships), linear regression can be used with one modification. Instead of predicting the values 0 if a goal isn't scored and 1 if it is, the model is trained on predicting *scaled goals*, which are calculated as $1/ \text{xG}$. Therefore, even though the model is incapable of accurate prediction of goals, the least-squares method can give us accurate $\alpha_i$ coefficients. To do this, rare goals scored from very low xG are excluded, so no scaled values are too large.

A variety of feature combinations were used. The models were sklearn's LinearRegression and ElasticNet. Two random features, rnd1 and rnd2 were inserted for control. 

Predicting penalties is mostly avoided. It is statistically sketchy, as calm and efficient players are always selected to take the penalty, and because the mental component is more important and probably should be modeled with different parameters. Therefore, including penalties would probably mess with the *linear* regression model.

The autoregressive property of the model is preserved (through great effort). 

## Caveat

It is possible that Understat's specific xG model already takes mental factors into account. If this is true, this analysis is mostly useless. 

## Results

![image](./Results.png)

The calculation methods of the features are available in the main notebook.

## Further work

Data from other leagues can be added easily after matching the team names used by OddsPortal and Understat. In addition, I suspect that many individual player features (like PrevAccumXG) are used by the model as proxies for the player's usual goalscoring ability or position, but I wasn't able to quantify this easily while preserving the autoregressive property - this can be done in the future.
