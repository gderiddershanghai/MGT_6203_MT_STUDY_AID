# SA1
question_1 = {
    'question': "In Ordinary Least Squares we are trying to minimize:",
    'options_list': ['The Median Absolute Error', 'The Mean Absolute Error', 'The Sum of Squared Error', 'The Root Mean Squared Error'],
    'correct_answer': 'The Sum of Squared Error',
    'chapter_information': 'Week 1, page 18 slide 1'
}

question_2 = {
    'question': "An indicator variable is sometimes referred to as a:",
    'options_list': ['Hyperparameter', 'Dummy variable', 'Interaction variable', 'Continuous predictor variable'],
    'correct_answer': 'Dummy variable',
    'chapter_information': 'Week 2, page 9 slide 2'
}

question_3 = {
    'question': "Which of the following is an example of an Interaction Term?",
    'options_list': ['Height*Gender', 'Height^2', 'Height - Gender', 'Height + Gender'],
    'correct_answer': 'Height*Gender',
    'chapter_information': 'Week 2, page 18 slide 1'
}

question_4 = {
    'question': "If your dataset has a column that contained one of three states for each observation ('New York', 'California', 'Hawaii'), what would be the best way to code them for a regression model with one-hot encoding?",
    'options_list': ['1 for New York, 2 for California, 3 for Hawaii', 'Assign a unique identifier for each state', 'Use binary indicators for each state', 'Encode each state with a different color'],
    'correct_answer': 'Use binary indicators for each state',
    'chapter_information': 'Week 2, page 24 slide 2'
}

# question_5 = {
#     'question': "How much more would a person in California expect to pay per day vs a person in New York of the same age, given the regression model and coefficients?",
#     'options_list': ['$5', '$-5', '$10', '$-15'],
#     'correct_answer': '$10',
#     'chapter_information': 'Week 2, Page 27 slide 2'
# }

question_6 = {
    'question': "In a linear regression model with one qualitative (categorical) predicting variable with 4 values, we need to include 4 dummy variables.",
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'chapter_information': 'Week 2, page 20 slide 2'
}

# question_7 = {
#     'question': "Based on the following regression model summary (Note: the base case is Age = Young), what is the Amount Spent by a Middle-aged customer if his/her salary is 10000?",
#     'options_list': ['20 – 6.12', '20 – 6.12 - 4.81', '20 – 6.12 +23.28', '20'],
#     'correct_answer': '20 – 6.12 - 4.81',
#     'chapter_information': 'Lesson 2 / Video 4 / Slides 1 – 4'
# }

question_8 = {
    'question': "An interaction term is used to model how the synergies between multiple variables impact the response variable.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'chapter_information': 'Lesson 2 / Video 4 / Slides 6 – 9'
}

# SA2
sa2_question_1 = {
    'question': "Select the equation that can be used for a linear-log model:",
    'options_list': ['Y = b0 + b1 * X', 'Y = b0 + b1 * log(X)', 'log(Y) = b0 + b1 * X', 'log(Y) = b0 + b1 * log(X)'],
    'correct_answer': 'Y = b0 + b1 * log(X)',
    'chapter_information': 'Module 3'
}

sa2_question_2 = {
    'question': "Select the equation that can be used for a log-log model:",
    'options_list': ['Y = b0 + b1 * X', 'Y = b0 + b1 * log(X)', 'log(Y) = b0 + b1 * X', 'log(Y) = b0 + b1 * log(X)'],
    'correct_answer': 'log(Y) = b0 + b1 * log(X)',
    'chapter_information': 'Module 3'
}

sa2_question_3 = {
    'question': "In regard to a linear-log model, increasing X by 1% is almost equivalent to which of the following:",
    'options_list': ['Increasing log(X) by 0.01 units', 'Decreasing (natural) log(X) by 0.01 units', 'Increasing (natural) log(X) by 0.01 units', 'Increasing x by one unit will increase (natural) log(y) by b1 units', 'None of the above'],
    'correct_answer': 'Increasing (natural) log(X) by 0.01 units',
    'chapter_information': 'Module 3'
}

sa2_question_4 = {
    'question': "Increasing (natural) log(X) by 0.01 leads to increasing (natural) log(Y) by b1 * 0.01 units best describes which model?",
    'options_list': ['Linear-Linear', 'Linear-Log', 'Log-Linear', 'Log-Log'],
    'correct_answer': 'Log-Log',
    'chapter_information': 'Module 3'
}

sa2_question_5 = {
    'question': "Which of the following results from the residual analysis of a linear regression model is not a clear signal for the need to explore non-linear models?",
    'options_list': ['The residuals vs. fitted values plot indicates that the model has heteroscedasticity',
                     'the QQ-plot suggest that there is non-linearity',
                     'The residuals suffer from non-constant variance',
                     'The residuals appear to be normally distributed.'],
    'correct_answer': 'The residuals appear to be normally distributed.',
    'chapter_information': 'Module 3, slide 4'
}

sa2_question_6 = {
    'question': "For a non-linear model salary = b0 + b1*log (years of experience). If b1 = 5122, which of the following statements is correct?",
    'options_list': ['When years of experience increases by 1, salary increases (on average) by $5122.', 'When years of experience decreases by 1, salary increases (on average) by $5122.',\
        'When years of experience increases by 1%, salary increases (on average) by $51.22.', 'When years of experience decreases by log (1), salary increases (on average) by $51.22.'],
    'correct_answer': 'When years of experience increases by 1%, salary increases (on average) by $51.22.',
    'chapter_information': 'Module 3, slide 8'
}

sa2_question_7 = {
    'question': "Which of the following could be a reason for applying log transformation on a dataset?",
    'options_list': ['To make a distribution more normal', 'To make the variance more constant', 'To get a better fit in the model – i.e. increase R-Squared', 'All of the above'],
    'correct_answer': 'All of the above',
    'chapter_information': 'Module 3, slide 16'
}

sa2_question_8 = {
    'question': "Consider the equation Cost = 4.3 + 6.89 *log(length). How should the length be increased such that the cost increases by 6.89 units?",
    'options_list': ['Increase length by 1 unit', 'Increase length by e units', 'Multiply length by e units', 'Increase length by 6.89 units'],
    'correct_answer': 'Multiply length by e units',
    'chapter_information': 'Module 3'
}

sa2_question_9 = {
    'question': "Consider the equation 3.45 log (Y) = 2.33 + 87.6 log(X). What is the elasticity?",
    'options_list': ['2.33', '87.6', '25.39', '3.45'],
    'correct_answer': '25.39',
    'chapter_information': 'Module 3, page 14'
}

sa2_question_10 = {
    'question': "Which of the following statements is FALSE about Polynomial Regression?",
    'options_list': [
        "Polynomial provides a better approximation of the relationship between the dependent and independent variable",
        "Presence of outliers can greatly influence results of the non-linear analysis",
        "The fitted model is more reliable when it is built on a larger sample size n",
        "It allows for an isolated interpretation of coefficients of non-linear variables"
    ],
    'correct_answer': "It allows for an isolated interpretation of coefficients of non-linear variables",
    'chapter_information': 'Module 3, page 19'
}

#sa 3 is all R

#sa4
sa4_question_1 = {
    'question': "What is the orthogonality assumption in OLS, taking Y = a + bX as the model, and error term is e?",
    'options_list': ['Correlation(X, X) = 0', 'Correlation(X, e) = 0', 'Correlation(e, X) = 1', 'None of the above'],
    'correct_answer': 'Correlation(X, e) = 0',
    'chapter_information': 'Week 5, Lesson 2'
}

sa4_question_2 = {
    'question': "While calculating a difference in difference, we run a regression which is as follows: lm( y ~ d1 +d2 + d3) where d1 and d2 are dummy variables and d3 is their interaction term. What is the difference in difference estimator?",
    'options_list': ['a+b+c+d', '(d-c)-(b-a)', 'a', 'd'],
    'correct_answer': 'd',
    'chapter_information': 'Module 5, Slide 20'
}

sa4_question_3 = {
    'question': "We want to observe a column 'y' in dataset. We divide the observations into 2 parts, where y_0 is the set of observations of control group and y_1 is the set of observations of treatment group. What is the difference estimator given by?",
    'options_list': ['mean(y_1) – mean(y_0)', 'Covariance(y_1, y_2)', '1 – mean(y_1)/mean(y_2)', 'Var(y_2)'],
    'correct_answer': 'mean(y_1) – mean(y_0)',
    'chapter_information': 'Module 5, Slide 8'
}

sa4_question_4 = {
    'question': "True or False: The weakest linear relationship is indicated by a correlation coefficient equal to -1.",
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'chapter_information': 'General knowledge'
}

sa4_question_5 = {
    'question': "Which of the following is an example of a natural experiment?",
    'options_list': ['One state, but not others, increases income tax', 'Changing store policy to allow online orders to be picked up in any store', 'A mobile carrier implements an unlimited data plan open to all customers', 'Testing new plant growth in different soil conditions in a lab'],
    'correct_answer': 'One state, but not others, increases income tax',
    'chapter_information': 'Definition in Slide 15'
}

sa4_question_6 = {
    'question': "Researchers compare the average change over time of the independent variable for the treatment group to the average change over time of the independent variable for the control group. This comparison is called difference in difference.",
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'chapter_information': 'Definition in Slide 15'
}

sa4_question_7 = {
    'question': "Which of the following is an indication that there is random assignment in an experiment?",
    'options_list': ['The coefficients of the regression model are all approximately equal to 1.', 'The intercept of the regression model is equal to 0.', 'The coefficients of the regression model are all significant.', 'The coefficients of the regression model are all insignificant.'],
    'correct_answer': 'The coefficients of the regression model are all insignificant.',
    'chapter_information': 'Module 5, Lesson 4'
}

sa4_question_8 = {
    'question': "The range of values of correlation is:",
    'options_list': ['[0,1]', '[-1,0]', '[-1,1]', '[-∞,∞]'],
    'correct_answer': '[-1,1]',
    'chapter_information': 'General knowledge'
}

sa4_question_9 = {
    'question': "To estimate the causal impact of a treatment, we need to compare the treatment outcome to the:",
    'options_list': ['Counterpoint', 'Counterfactual', 'Correlation', 'Confusion Matrix'],
    'correct_answer': 'Counterfactual',
    'chapter_information': 'Module 5, Lesson 5'
}

sa4_question_10 = {
    'question': "How can selection bias be avoided?",
    'options_list': ['Randomized controlled experiment', 'Natural experiment', 'Add control variables', 'All the above'],
    'correct_answer': 'All the above',
    'chapter_information': 'Week 5, slide 6'
}



### hw1
hw1_question_1 = {
    'question': "Which of the following indicate that the result from a simple linear regression model could be potentially misleading?",
    'options_list': [
        'The dependent and the independent variable show a linear pattern.',
        'The error terms exhibit homoscedasticity',
        'The error terms follow a normal distribution',
        'The nth error term could be predicted with e_n = 0.91*e_{n-1}'
    ],
    'correct_answer': 'The nth error term could be predicted with e_n = 0.91*e_{n-1}',
    'chapter_information': 'Homework 1'
}

hw1_question_2 = {
    'question': "Consider a multiple linear regression model: Y = 0.55 + 0.93*x1 + 1.88*x2. Which of the following interpretation of the coefficients is correct?",
    'options_list': [
        'A unit increase in x1 is associated with an 0.93 increase in Y.',
        'Y is predicted to be equal to 0.55 when both x1 and x2 take the value of 1',
        'A unit increase in x2 is associated with a 1.88 increase in Y, keeping all else constant.',
        'A 0.93 increase in x1 is associated with a 1.88 increase in x2'
    ],
    'correct_answer': 'A unit increase in x2 is associated with a 1.88 increase in Y, keeping all else constant.',
    'chapter_information': 'Homework 1'
}

hw1_question_3 = {
    'question': "When testing our predictive variables for Multicollinearity we create a model in R of lm(pred1 ~ pred2 + pred3, data = dataset) and we get an R Squared of 0.85. What is the VIF for pred1?",
    'options_list': [
        '0.85',
        '0.15',
        '6.667',
        '0.5405'
    ],
    'correct_answer': '6.667',
    'chapter_information': 'Homework 1'
}

hw1_question_4 = {
    'question': "Consider a linear regression model estimating the fuel efficiency of a car in terms miles per gallon of gas (mpg) based on its origin (region A, B or C) \
        and number of cylinders with the following formula: mpg = b0 + b1*RegionB + b2*RegionC + b3*Cylinders. The estimated values of the regression coefficients are provided below: b0 = 40.7, b1 = -0.91, b2 = 2.66, b3 = -3.15. Based on this model, \
            if X is the mpg of a car with 4 cylinders originated from region B, and Z is the mpg of a car with 3 cylinders originated from region A, what is the value of X - Z:",
    'options_list': [
        '-0.91',
        '-3.15',
        '-4.06',
        '-6.72'
    ],
    'correct_answer': '-4.06',
    'chapter_information': 'Homework 1'
}

hw1_question_5 = {
    'question': "True or False, when you create a linear regression model with factors (i.e. male, female), R converts those factors into dummy variables?",
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'chapter_information': 'Homework 1'
}

hw1_question_6 = {
    'question': "From the following regression model: Gold_Price_Per_oz = B0 + B1*M2+B2*VIX+B3*War, where M2 is a continuous variable of the M2 money supply, VIX is a continuous variable of the VIX index, and War is a categorical variable (0 is Time period at peace, 1 is Time period at war). Which of the following would be a part of the base case conditions?",
    'options_list': [
        'Time period at war',
        'Time period at peace',
        'A high VIX index',
        'Period of inflation'
    ],
    'correct_answer': 'Time period at peace',
    'chapter_information': 'Homework 1'
}

hw1_question_7 = {
    'question': "Given the following model: price = b0 + b1*lotsize + b2*lotsize^2, how can one interpret the coefficients? Select the best answer.",
    'options_list': [
        'Price increases by b0 + b1 + b2^2 when lotsize is increased by 1 unit.',
        'A quadratic model does not allow for an isolated interpretation of coefficients.',
        'Price increases by b1 when lotsize is increased by 1 unit.',
        'Price increases by b2 when lotsize is increased by 1 unit.'
    ],
    'correct_answer': 'A quadratic model does not allow for an isolated interpretation of coefficients.',
    'chapter_information': 'Homework 1'
}

hw1_question_8 = {
    'question': "Select the model approximation that best matches the following statement: 'As X increases by 1%, Y increases by (b1/100) units, holding all other factors constant.'",
    'options_list': [
        'Y = b0 + b1*X',
        'Y = b0 + b1*log(X)',
        'log(Y) = b0 + b1*X',
        'log(Y) = b0 + b1*log(X)'
    ],
    'correct_answer': 'log(Y) = b0 + b1*X',
    'chapter_information': 'Homework 1'
}

hw1_question_9 = {
    'question': "Assume that you have concluded to use a log transformation on your data to model a relationship. However, on investigating the dataset, you found negative and zero values. How will you proceed?",
    'options_list': [
        'Throw out the data points which are negative or zero',
        'Use Log(x+1), where x is the variable you want to transform',
        'Use log(x + c +1), where c is the absolute value of the most negative number',
        'Use log(10 * x)'
    ],
    'correct_answer': 'Use log(x + c +1), where c is the absolute value of the most negative number',
    'chapter_information': 'Homework 1'
}

hw1_question_10 = {
    'question': "If we decrease the cutoff value and then consider that the number of true positives, true negatives, false positives, and false negatives changes, which of the following is true?",
    'options_list': [
        'False positive rate decreases',
        'Sensitivity increases',
        'Specificity increases',
        'None of the above'
    ],
    'correct_answer': 'Sensitivity increases',
    'chapter_information': 'Homework 1'
}

hw1_question_12 = {
    'question': "Which of the following case is referred to Type II error?",
    'options_list': [
        'Null is false and we reject it.',
        'Null is True, but we fail to reject it.',
        'Null is True but we mistakenly reject it.',
        'Null is false but we fail to reject it.'
    ],
    'correct_answer': 'Null is false but we fail to reject it.',
    'chapter_information': 'Homework 1'
}
######## hw2
hw2_part1_q1 = {
    'question': "Given a complete deck of cards, the probability of drawing the Ace of Diamonds is 1/52. Based on this probability, what are the odds for this event?",
    'options_list': ['1/51', '1/52', '51/1', '52/1'],
    'correct_answer': '1/51',
    'chapter_information': 'Odds(for) = p/(1−p) = (1/52)/(1−1/52) = 1/51'
}

hw2_part1_q2 = {
    'question': "Which of the following is the reason why linear regression is not suitable for modelling binary responses?",
    'options_list': [
        'With a linear regression model, all predicted outcomes will fall between zero and one.',
        'With a linear regression model, some of the predicted outcomes may be less than zero or greater than one.',
        'Linear regression is not capable of modelling a response based on more than one variable at a time.',
        'Linear regression is not capable of modelling categorical variables.'
    ],
    'correct_answer': 'With a linear regression model, some of the predicted outcomes may be less than zero or greater than one.',
    'chapter_information': 'Lecture slide #8'
}

hw2_part1_q3 = {
    'question': "If we decrease the cutoff value of a logistic regression model then considering that number of True positives, True negatives, False positive and False negatives changes, which of the following is true? (Assume that there are no changes in the dataset used)",
    'options_list': [
        'False positive rate decreases',
        'Sensitivity increases',
        'Specificity increases',
        'None of the above'
    ],
    'correct_answer': 'Sensitivity increases',
    'chapter_information': "Module 4: As we decrease the cutoff value, the number of True positives \
    increase, the number of True negatives decrease, the number of False positives increase and \
    the number of False negatives decrease. Since the (number of True positives + number of \
    False negatives) = Actual positives and (number of True negatives + False positives) = Actual \
    negatives remain the same as we're using the same dataset, Sensitivity increases, Specificity \
        decreases and False positive rate increases. "
}

hw2_part1_q4 = {
    'question': "After running a logistic linear regression model in R where logit(p) = b0 + b1*student, you find that your coefficient estimate for your ‘non-students’ (intercept) is equal to –4.732 and your coefficient estimate for ‘student’ is equal to 1.748. Calculate the odds for non-students and students.",
    'options_list': [
        'e(-4.732), e(-4.732+1.748)',
        '-4.732, -4.732+1.748',
        '-4.732, 1.748',
        'log(-4.732), log(1.748)'
    ],
    'correct_answer': 'e(-4.732), e(-4.732+1.748)',
    'chapter_information': 'Module 4 (Page 17 Slide 2)'
}

hw2_part1_q5 = {
    'question': "Which of the following is not needed to establish causation?",
    'options_list': [
        'Hypothesized cause must precede its anticipated effect.',
        'Other possible explanations that can cause the effect must be ruled out.',
        'Change in cause must lead to a change in effect.',
        'The effect must always have a reverse impact on the cause.'
    ],
    'correct_answer': 'The effect must always have a reverse impact on the cause.',
    'chapter_information': '(Module 5, slide 3)'
}

hw2_part1_q7 = {
    'question': "Choose if the following statement is true or false: Correlation is sensitive to the scale of the data; however, covariance is not sensitive to the scale of the data.",
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'chapter_information': 'Correlation is NOT sensitive to the scale and covariance is scale sensitive à If we scale each random variable (say X and Y) by the same factor (say 2), \
        the relative position of data won’t change, but the covariance between X and Y becomes 4 times which can be confirmed by the formula. However, in case of correlation – \ it has \
            normalizing standard deviation terms in denominator which makes it immune to the scale of data.'
}

hw2_part1_q8 = {
    'question': "Which of the following is NOT an example of selection bias?",
    'options_list': [
        'A voter survey to predict vote distribution for the presidential election in the US which is based on a sample of low-income household voters in the US.',
        'Taking surveys of people to participate in the study over email.',
        'Survey filled by audiences who have come to see radio/tv shows that are on controversial topics (abortion, affirmative action, gun control, etc.).',
        'Dividing states into subgroups based on important characteristics and randomly selecting houses to be surveyed.'
    ],
    'correct_answer': 'Dividing states into subgroups based on important characteristics and randomly selecting houses to be surveyed.',
    'chapter_information': '. D. is the only part where there is no selection bias for a state-wide survey. A is an example of Under-coverage Bias; B is an example of Nonresponse Bias and C is an example of Voluntary Response Bias.'
}

hw2_part1_q10 = {
    'question': "Suppose you invested in a fund for 1 year. The fund return was 10% and risk-free rate was 2%. The fund’s standard deviation over this period was 5% and beta was 1.3. What was the fund’s Sharpe ratio?",
    'options_list': ['0.06', '1.6', '4', '6.15'],
    'correct_answer': '1.6',
    'chapter_information': 'Sharpe Ratio = (0.10 – 0.02)/0.05 = 1.6'
}

hw2_part1_q11 = {
    'question': "Given beta (β) of the following stocks, which stock would have the most increase if the market has a 10% increase?",
    'options_list': [
        'Stock A beta = 1',
        'Stock B beta = 1.8',
        'Stock C beta = 0.1',
        'Stock D beta = -1.5'
    ],
    'correct_answer': 'Stock B beta = 1.8',
    'chapter_information': "Beta measures sensitivity and how the stock co-moves with changes in the market. If beta = 1, \
        then stock price moves up 1% in each 1% increase in market. If beta = 0, then stock price stays unchanged with each 1% increase in market. If beta > 1, then stock price moves greater than the 1% increase in market. \
            In this question, Stock B has the highest positive beta. A 10% increase in market would result in 18% (10% * 1.8) increase to the stock price"
}

hw2_part1_q12 = {
    'question': "Consider 2 stocks A and B. Over a period of time, the Jensen’s alpha for stock A was 0.5 and the Jensen’s alpha for stock B was -0.7. Given the beta for stock A was 1.2 and for stock B was 1.5, and considering that the return on the index used in calculating Jensen’s alpha and beta for these stocks over this time period was the same as the risk-free rate, which stock had better return over this period of time?",
    'options_list': [
        'Stock A',
        'Stock B',
        'Can’t say as more information is required to make this decision'
    ],
    'correct_answer': 'Stock A',
    'chapter_information': 'Since the return of the market index is same as the risk-free rate, the multiplier of the beta term (Rm-Rf) is zero and hence beta has no effect over the returns of these stocks. Since the error terms are insignificant, the stock with higher alpha has higher excess returns and hence has higher returns.'
}




COURSE_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        COURSE_MPC_QUESTIONS.append(value)

COURSE_MPC_QUESTIONS = COURSE_MPC_QUESTIONS[:-1]
