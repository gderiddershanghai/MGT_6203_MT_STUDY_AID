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

question_5 = {
    'question': "How much more would a person in California expect to pay per day vs a person in New York of the same age, given the regression model and coefficients?",
    'options_list': ['$5', '$-5', '$10', '$-15'],
    'correct_answer': '$10',
    'chapter_information': 'Week 2, Page 27 slide 2'
}

question_6 = {
    'question': "In a linear regression model with one qualitative (categorical) predicting variable with 4 values, we need to include 4 dummy variables.",
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'chapter_information': 'Week 2, page 20 slide 2'
}

question_7 = {
    'question': "Based on the following regression model summary (Note: the base case is Age = Young), what is the Amount Spent by a Middle-aged customer if his/her salary is 10000?",
    'options_list': ['20 – 6.12', '20 – 6.12 - 4.81', '20 – 6.12 +23.28', '20'],
    'correct_answer': '20 – 6.12 - 4.81',
    'chapter_information': 'Lesson 2 / Video 4 / Slides 1 – 4'
}

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
    'options_list': ['The residuals vs. fitted values plot indicates that the model has heteroscedasticity', 'the QQ-plot suggest that there is non-linearity', 'The residuals suffer from non-constant variance', 'The residuals appear to be normally distributed.'],
    'correct_answer': 'The residuals appear to be normally distributed.',
    'chapter_information': 'Module 3, slide 4'
}

sa2_question_6 = {
    'question': "For a non-linear model salary = b0 + b1*log (years of experience). If b1 = 5122, which of the following statements is correct?",
    'options_list': ['When years of experience increases by 1, salary increases (on average) by $5122.', 'When years of experience decreases by 1, salary increases (on average) by $5122.', 'When years of experience increases by 1%, salary increases (on average) by $51.22.', 'When years of experience decreases by log (1), salary increases (on average) by $51.22.'],
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


COURSE_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        COURSE_MPC_QUESTIONS.append(value)
