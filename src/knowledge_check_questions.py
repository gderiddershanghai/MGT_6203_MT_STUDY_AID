###########knowledge check 1############################
kc1_question_1 = {
    'question': "Given R squared is 0.68. Find the adjusted R squared if the sample size is 600 and number of independent variables is 10.",
    'options_list': ['0.676', '0.688', '0.667', '0.674'],
    'correct_answer': '0.674',
    'chapter_information': 'Week 1, Slide 31'
}

kc1_question_2 = {
    'question': "Which of the following values cannot be an R squared value?",
    'options_list': ['0.5', '0.99', '.003', '1.2'],
    'correct_answer': '1.2',
    'chapter_information': 'Week 1, Slide 20'
}

kc1_question_3 = {
    'question': "The total deviation at observation (xi, yi) is:",
    'options_list': ['ŷi - ȳi', 'yi - ȳ', 'yi - ŷi', 'None of these'],
    'correct_answer': 'yi - ȳ',
    'chapter_information': 'Week 1, Slide 17'
}

kc1_question_4 = {
    'question': "How can we detect multicollinearity in a model?",
    'options_list': ['Variance Inflation factor (VIF)', 'Correlation matrix', 'R2', 'Both a) and b)'],
    'correct_answer': 'Both a) and b)',
    'chapter_information': 'Week 1, Slide 45-46'
}


###########knowledge check 2############################

kc2_question_1 = {
    'question': "If you convert a categorical variable with M categories into dummy variables, how many dummy variables are created?",
    'options_list': ['M – 2', 'M', 'M – 1', 'None of the above'],
    'correct_answer': 'M – 1',
    'chapter_information': 'Lesson 2 / Video 2 / Slides 3 –5'
}

kc2_question_2 = {
    'question': "Based on the following regression model summary (Note: the base case is Age = Young), what is the Amount Spent by a Middle-aged customer if his/her salary is 10000?",
    'options_list': ['20-6.12', '20 – 6.12 - 4.81', '20 – 6.12 + 23.28', '20'],
    'correct_answer': '20 – 6.12 - 4.81',
    'chapter_information': 'Lesson 2 / Video 4 / Slides 1 – 4'
}

kc2_question_3 = {
    'question': "An interaction term is used to model how the synergies between multiple variables impact the response variable.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'chapter_information': 'Lesson 2 / Video 4 / Slides 6 – 9'
}

###########knowledge check 3############################
kc3_question_1 = {
    'question': "Using the following regression equation, determine which statement is correct.\n\nPrice = b0 + b1*lotsize + b2*lotsize^2",
    'options_list': [
        "Coefficients b1 and b2 can be interpreted individually because when lotsize is increased by 1 unit, it is not possible (or meaningful) to hold lotsize^2 constant.",
        "Coefficients b1 and b2 can be interpreted individually because when lotsize is decreased by 1 unit, it is not possible (or meaningful) to hold lotsize^2 constant.",
        "Coefficients b1 and b2 cannot be interpreted individually because when lotsize is increased by 1 unit, it is not possible (or meaningful) to hold lotsize^2 constant.",
        "Coefficients b1 and b2 cannot be interpreted individually because when lotsize is increased by 1 unit, it is possible (or meaningful) to hold lotsize^2 constant."
    ],
    'correct_answer': 'Coefficients b1 and b2 cannot be interpreted individually because when lotsize is increased by 1 unit, it is not possible (or meaningful) to hold lotsize^2 constant.',
    'chapter_information': 'Lesson 3 / Video 5 / Slide 3'
}

kc3_question_2 = {
    'question': "Increasing X by 1 percent is almost equivalent to increasing (natural) log(X) by 0.01 units.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'chapter_information': 'Lesson 3 / Video 2 / Slide 3'
}

kc3_question_3 = {
    'question': "What type of plot do you see in the following image?",
    'options_list': ['Residuals vs Fitted', 'Normal Q-Q', 'Scale -Location', 'Residuals vs Leverage'],
    'correct_answer': 'Normal Q-Q',
    'chapter_information': 'Lesson 3 / Video 2 / Slide 5'
}

kc3_question_4 = {
    'question': "Which of the following are the main purposes of log-transformation? Choose all the right answers.",
    'options_list': [
        "Achieve a more exponential relationship",
        "Make a distribution more normal",
        "Increase the variance"
    ],
    'correct_answer': ['Make a distribution more normal'],
    'chapter_information': 'Lesson 3 / Video 4 / Slide 7'
}

kc3_question_5 = {
    'question': "Which of the following are the main purposes of log-transformation? Choose all the right answers.",
    'options_list': [
        "Achieve a more exponential relationship",
        "Increase the variance",
        "Get a better fit such as higher R-squared"
    ],
    'correct_answer': ['Get a better fit such as higher R-squared'],
    'chapter_information': 'Lesson 3 / Video 4 / Slide 7'
}

###########knowledge check 4############################
kc4_question_1 = {
    'question': "If we want to arrive at the model given below:\n\ny = b0 + b1x1 + b2x2,\nwhere y is a continuous response variable in range (0,1) while x1 and x2 are binary predictors (with discrete values 0 or 1), what is the correct regression to be used:",
    'options_list': ['Simple linear regression', 'Multiple linear regression', 'Logistic regression', 'None of the above'],
    'correct_answer': 'Multiple linear regression',
    'chapter_information': 'Explanation: Since response variable is continuous and we have multiple predictors, we should use multiple linear regression.'
}

kc4_question_2 = {
    'question': "Which of the following is type 1 error?",
    'options_list': [
        "A null hypothesis is rejected when it should not be rejected",
        "A null hypothesis is not rejected when it should be rejected",
        "When p value is above a threshold",
        "When p value is below a threshold"
    ],
    'correct_answer': 'A null hypothesis is rejected when it should not be rejected',
    'chapter_information': 'Module 4, slide 27'
}

kc4_question_3 = {
    'question': "Which of the following generally takes place when we increase the cutoff value of p?",
    'options_list': ['Sensitivity increases', 'Specificity decreases', 'Precision increases', 'Recall increases'],
    'correct_answer': 'Precision increases',
    'chapter_information': 'Precision increases when we increase the classification threshold. Others are incorrect. Module 4, slide 29'
}

kc4_question_4 = {
    'question': "For the given logistic regression model output, select the correct option (Smoker is a categorical variable with 2 levels: Smoker/Non-Smoker):",
    'options_list': [
        "For smokers versus non-smokers, the odds of survival is ~21.4% lower than for non-smokers; assuming all else constant",
        "For smokers versus non-smokers, the log odds of survival decreases by 7.54; assuming all else constant",
        "For smokers versus non-smokers, the odds of survival decreases by 0.24; assuming all else constant",
        "None of these"
    ],
    'correct_answer': 'For smokers versus non-smokers, the odds of survival decreases by 0.24; assuming all else constant',
    'chapter_information': 'Correct interpretation of logistic regression model output regarding the effect of smoking on survival odds.'
}

###########knowledge check 5############################
kc5_question_1 = {
    'question': "A correlation of 1 means that there is a strong correlation and causation between two variables.",
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'chapter_information': 'Lesson 1, Slide 4'
}

kc5_question_2 = {
    'question': "Which of the following approaches is a good way to avoid selection bias?",
    'options_list': ['Self-Selection', 'Voluntary-response', 'Random sampling', 'None of the above'],
    'correct_answer': 'Random sampling',
    'chapter_information': 'Lesson 2, slide 2,5'
}

kc5_question_3 = {
    'question': "Which of the following is not an example of a natural experiment?",
    'options_list': [
        "A law that changed the tax rate for some subjects, but not others",
        "Minimum wage is changed in one state but not another",
        "A mobile carrier implements an unlimited data plan in some cities but not others",
        "A hurricane that hits all the stores countrywide"
    ],
    'correct_answer': 'A hurricane that hits all the stores countrywide',
    'chapter_information': 'Lesson 5, slide 2'
}

###########knowledge check 6############################

kc6_question_1 = {
    'question': "Does the market value of a company change after a 2 for 1 stock split?",
    'options_list': ['Yes', 'No'],
    'correct_answer': 'No',
    'chapter_information': 'Lesson 1: Simple and Compound Returns'
}

kc6_question_2 = {
    'question': "Which of the following represents the cumulative effect that a series of gains or losses has on an original investment over a period of time?",
    'options_list': ['Simple Return', 'Compound Return'],
    'correct_answer': 'Compound Return',
    'chapter_information': 'Lesson 1 / Slide 6'
}

kc6_question_3 = {
    'question': "Which of the following is not a measure of risk?",
    'options_list': ['Standard Deviation', 'Beta', 'Drawdown', 'Stock split'],
    'correct_answer': 'Stock split',
    'chapter_information': 'Lesson 2 / Slide 1'
}

kc6_question_4 = {
    'question': "What Beta represents a risk-free asset?",
    'options_list': ['0', '1', '2'],
    'correct_answer': '0',
    'chapter_information': 'Lesson 2 / Slide 7'
}

kc6_question_5 = {
    'question': "What measures sensitivity to market movements?",
    'options_list': ['Standard Deviation', 'Beta'],
    'correct_answer': 'Beta',
    'chapter_information': 'Lesson 2 / Slide 6'
}

kc6_question_6 = {
    'question': "Which of the following asset classes has the highest standard deviation over time?",
    'options_list': ['Bonds', 'Inflation', 'Small Cap'],
    'correct_answer': 'Small Cap',
    'chapter_information': 'Lesson 3 / Slide 5'
}

###########knowledge check 7############################
kc7_question_1 = {
    'question': "Which of the following measures risk adjusted performance?",
    'options_list': ['Sharpe Ratio', 'Treynor Ratio', 'Jensen’s Alpha', 'All of the above'],
    'correct_answer': 'All of the above',
    'chapter_information': 'Lesson 1 / Slide 1'
}

kc7_question_2 = {
    'question': "What does Jensen’s Alpha measure?",
    'options_list': [
        "Abnormal return by comparing to a benchmark",
        "Investment reward per unit risk",
        "Abnormal return that the portfolio earns after adjusting beta"
    ],
    'correct_answer': "Abnormal return by comparing to a benchmark",
    'chapter_information': 'Lesson 1 / Slide 8'
}

kc7_question_3 = {
    'question': "True or False: Transaction costs always lower our returns.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'chapter_information': 'Lesson 2 / Slide 8'
}

kc7_question_4 = {
    'question': "What is the bid-ask spread of stock symbol XYZ given the best ask price is $36 and best bid price is $34?",
    'options_list': ['$1', '$2', '$35', '$70'],
    'correct_answer': '$2',
    'chapter_information': 'Lesson 2 / Slides 4-5'
}

kc7_question_5 = {
    'question': "Which of the following transaction cost describes this scenario? An investor pays a fixed $5.00 fee per trade.",
    'options_list': ['Commissions', 'Bid-Ask Spread Cost', 'Delay Cost'],
    'correct_answer': 'Commissions',
    'chapter_information': 'Lesson 2 / Slide 4'
}

kc7_question_6 = {
    'question': "Which of the following is not a type of market efficiency?",
    'options_list': ['Weak Form', 'Semi-Weak Form', 'Semi-Strong Form', 'Strong Form'],
    'correct_answer': 'Semi-Weak Form',
    'chapter_information': 'Lesson 3 / Slide 1'
}

kc7_question_7 = {
    'question': "If the current stock price reflects all publicly available information and not private information, what type of market efficiency is it experiencing?",
    'options_list': ['Weak Form', 'Semi-Weak Form', 'Semi-Strong Form', 'Strong Form'],
    'correct_answer': 'Semi-Strong Form',
    'chapter_information': 'Lesson 3 / Slide 6'
}

kc7_question_8 = {
    'question': "The tendency of individuals to seek pride and avoid regret in their decisions is known as ______?",
    'options_list': ['Overconfidence', 'Loss Aversion', 'Recency Effect', 'Anchoring'],
    'correct_answer': 'Anchoring',
    'chapter_information': 'Lesson 4 / Slide 4'
}

kc7_question_9 = {
    'question': "XYZ’s stock price was trading at $50 last week. XYZ is trading at $40 today. You decided to purchase 1 share of XYZ at $40 because you think it will go back up to $50. You made the purchase even though you have no other evidence to suggest the valuation of XYZ should be at $50. What is this an example of?",
    'options_list': ['Overconfidence', 'Loss Aversion', 'Recency Effect', 'Anchoring'],
    'correct_answer': 'Anchoring',
    'chapter_information': 'Lesson 4 / Slide 4'
}
###########knowledge check 8############################
kc8_question_1 = {
    'question': "Which of the following statements is NOT true:",
    'options_list': [
        "A high B/M ratio stock is often called a value stock",
        "A low B/M ratio stock is often called a growth stock",
        "A low B/M ratio means the stock is inexpensive",
        "A high B/M ratio means the stock is inexpensive"
    ],
    'correct_answer': "A low B/M ratio means the stock is inexpensive",
    'chapter_information': "Explanation: C: A low B/M ratio means the stock is inexpensive is False."
}

kc8_question_2 = {
    'question': "Which of the following statements is/are a benefit of factor analysis?",
    'options_list': [
        "Investors can analyze what type of factors drove a stock’s performance over a period",
        "Investors can attribute performance of funds and fund managers to specific factor exposures",
        "Investors can construct more balanced portfolios",
        "Investors can better understand their portfolio’s exposure to factors",
        "All of the Above"
    ],
    'correct_answer': "All of the Above",
    'chapter_information': "Solution: E: All of the Above."
}

kc8_question_3 = {
    'question': "Which of the following coefficients indicates the fund is tilted towards growth stocks?",
    'options_list': [
        "A positive coefficient on BAB",
        "A negative coefficient on BAB",
        "A positive coefficient on HML",
        "A negative coefficient on HML"
    ],
    'correct_answer': "A negative coefficient on HML",
    'chapter_information': "Solution: D A negative coefficient on HML."
}

kc8_question_4 = {
    'question': "True or False? Each of the factors discussed in the lecture have experienced prolonged periods of underperformance.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'chapter_information': "Solution: A: True."
}

kc8_question_5 = {
    'question': "What is Sharpe Ratio used for?",
    'options_list': [
        "To calculate stocks and mutual fund return rates",
        "To determine stocks and mutual fund risk",
        "To identify stocks and mutual funds risk adjusted return",
        "To determine what drives the stocks and mutual funds returns"
    ],
    'correct_answer': "To identify stocks and mutual funds risk adjusted return",
    'chapter_information': "Solution: C: To identify stocks and mutual funds risk adjusted performance."
}

kc8_question_6 = {
    'question': "Which of the following is NOT a metric discussed in lecture of stock or portfolio performance?",
    'options_list': ['Sharpe Ratio', 'Jensen’s Alpha', 'Treynor Ratio', 'Case-Shiller Index'],
    'correct_answer': 'Case-Shiller Index',
    'chapter_information': "Solution: D: Case-Shiller Index; This is not a topic covered in the lectures."
}
