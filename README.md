# Crop Yield and Price Prediction Using Machine Learning Algorithms
 
 
PROBLEM STATEMENT

Based on prior crop yield, nutrients supplied, fertilizers used, climatic conditions to achieve high crop yield and predicting the best crops that yield the highest value for the upcoming cultivating season.
 
 
Crop Yield and Price Prediction

Crop Yield Prediction is a major problem in agriculture. Several supportive decisions for the crop's yield can be made with the aid of machine learning and deep learning approaches. In this situation, a variety of machine learning techniques can be used. Crop yield forecasting is crucial for agricultural planning. It is crucial to forecast crop yields for all crops at the beginning of each growing season, especially for agricultural planners who aim for higher yields each year. The farmer's actions regarding irrigation techniques, pest and fertilizer applications, crop rotation, and land preparation can occasionally also affect the yield. Additionally, some uncontrolled elements like the climate, pests, and subsidies can also affect the crop's production. Making predictions before the season would provide the farmers a plan of action for dealing with these issues. The farmer can choose which crop will bring in more money by estimating the crop's price at harvest.
 
 
PROPOSED METHODOLOGY

The following methodology is currently being suggested for the current project. The entire process begins with the definition of the issue statement and continues through the deployment of the solution and assistance to the user. According to the problem statement, pertinent information is gathered from government agencies that are open for non-commercial use. Datasets are thoroughly processed after data collection by removing unnecessary and redundant features. One dataset comprising all of the data is created by combining all of the smaller datasets after the datasets have been fully processed. The actual dataset is created, and after that, it is subjected to data visualization to uncover hidden patterns and insights. Once the data has been visualized, we may choose which machine learning techniques to employ in order to provide fresh yield forecasts. The performance of several machine learning models is tested, and the best model is then placed into production after being fine-tuned. creating a small website or app that uses the model to provide predictions to farmers as well as current market data and prices.
The methodology, in brief, is as below:
• Problem Identification
• Data Collection
• Dataset Processing
• Data Visualization to gain insights
• Getting the data ready for training
• Training the machine learning models
• Finalizing the model that gives best crop yield
• Relating the crop yield with current and probable future market prizes


MACHINE LEARNING MODELS AND METRICS

Machine Learning Algorithms:
The current project is based on regression. In order to compare various regression models, including
Linear Regression, Decision Tree Regression, Random Forest Regression, Gradient Boosting
Regression, and Linear SVR, they were utilised.

Linear Regressor:
Finding the link between a dependent variable and one or more independent variables is the process
of linear regression. The method in a linear regression challenge seeks to fit a straight line to the
input data. The goal of the linear regression procedure is to determine which line fits the data the
best by estimating the coefficients of the line.
Each regression algorithm has a unique approach to handling regression problems. When the dataset
has a large number of features, algorithms like Ridge Regression and Lasso Regression, which are
more regularised versions of Linear Regression, can be utilised (or unwanted features). However,
there are just 7 features to focus on for the current dataset. In this situation, they function almost
identically to the linear regression approach.

Decision Tree Regressor:
Regression is constructed using the Decision Tree Regressor as a tree structure. It divides a dataset
into ever-tinier subsets while concurrently producing the associated decision tree. The decision
nodes and leaf nodes are the two different sorts of nodes in the tree. The root node of a decision tree
is the node at the top. Both category and numerical data can be processed using decision trees. A
decision tree's tendency to overfit the data is a common drawback.

Random Forest Regressor:
For decision-making, Random Forest combines several Decision Trees. A forest of "Randomly
generated Decision Trees" makes up this algorithm. The decision tree method's overfitting flaw can
be remedied with the random forest approach. In comparison to previous regression models, this
approach is faster and more reliable.

Gradient Boosting Regressor:
A good machine learning approach for creating prediction models is gradient boosting. An additive model, a weak learner, and a loss function make up this algorithm's three components. The predictions are made using the weak learner. In the additive model, numerous weak learners are added. The loss function is minimised as a result of this addition. A training dataset can be quickly overfit using the gradient boosting approach.

Linear Support Vector Regressor (SVR):
Linear Support Vector Regressor lets us define how much error is acceptable in our model. It locates a line or hyperplane (for greater dimensions) that is suitable for fitting the data.

Training Using Cross-Validation:
By training the models on various subsets of the available data and evaluating them on the complementary collection of data, cross-validation evaluates ML models. In K Fold cross-validation, k subsets of the data are created. While the data will be trained on the k-1 other subsets, a different subset will be picked each time for evaluation. Given that almost all of the data is used to train and test the model, this procedure can reduce both variance and bias. In the current project, k = 10 was taken into account.

Performance Measures:
Performance measurements are present in every machine learning pipeline in some manner. You can determine the model's effectiveness on the data by looking at these performance measures. Regression techniques are known to forecast a continuous value. Therefore, performance measurements that measure the gap between the actual value and the anticipated value are necessary for regression algorithms. Some of the performance metrics applied to this project are listed below.

Mean Square Error (MSE):
The square root of the difference between the actual value and the predicted value is found by the mean squared error formula. One of the most used measures for regression jobs is this one.

Root Mean Squares Error (RMSE):
The square root of the mean squared error is equivalent to the term "Root Mean Squared Error" (MSE).
It is utilised to take into consideration the drawbacks of the Mean Squared Error. It is utilised to take into consideration the drawbacks of the Mean Squared Error. Because it can accommodate smaller errors that the mean squared error cannot, it is differentiable.

R2 (R-Squared) Coefficient of Determination:
R2 Coefficient of determination is a metric that is calculated using other metrics. This is calculated using the sum of squared errors. If R2 is near to 1 (ideal), the regression effectively captured all of the target's variance. On the other hand, if R2 is near to 0, the regression was unable to account for any variance in the target variable. R2 has a range of (-∞, 1). R2 can occasionally be negative, indicating that the regression was unable to adequately interpret the data.
