islr_c2_q1 = {
    'question': "Describe the difference between input and output variables in the context of statistical learning. Provide examples of each from the scenario described.",
    'correct_answer': "In statistical learning, input variables (also known as predictors, independent variables, features, or attributes) are the variables used to predict or explain the outcome of interest. Output variables (also known as response or dependent variables) are the outcomes or the variables being predicted or explained. For example, in a study predicting house prices, the input variables could include square footage, number of bedrooms, and location, while the output variable would be the price of the house.",
    'chapter_information': 'ISLR C2, Week 1'
}

islr_c2_q2 = {
    'question': "What is the general form of the relationship between a quantitative response Y and predictors X1, X2, …, Xp? How does the error term ε play a role in this relationship?",
    'correct_answer': "The general form of the relationship is Y = β0 + β1X1 + β2X2 + … + βpXp + ε, where Y is the quantitative response, X1, X2, …, Xp are the predictors, β0 is the intercept term, β1, β2, …, βp are the coefficients of the predictors, and ε is the error term. The error term represents the deviation of the actual responses from the predictions made by the linear relationship due to factors not included in the model.",
    'chapter_information': 'ISLR C2, Week 1'
}

islr_c2_q3 = {
    'question': "Discuss the concepts of 'reducible' and 'irreducible' error in the context of predicting Y using X. Why can't we eliminate irreducible error?",
    'correct_answer': "In statistical learning, 'reducible' error refers to the part of the prediction error that can be reduced or eliminated by using a more appropriate model or including more predictors. 'Irreducible' error, on the other hand, is the part of the error that cannot be reduced no matter how well the model is designed, because it arises from randomness or inherent variability in the system being modeled. We can't eliminate irreducible error because it is caused by factors outside our control or knowledge.",
    'chapter_information': 'ISLR C2, Week 1'
}

islr_c2_q4 = {
    'question': "Compare and contrast the goals of prediction and inference in statistical learning. Provide examples of scenarios where one might be preferred over the other.",
    'correct_answer': "The goal of prediction is to accurately forecast unseen data points, focusing on the relationship between the input and output variables without necessarily understanding the nature of this relationship. Inference, however, aims to understand the relationship between inputs and outputs, identifying how changes in the predictors affect the response variable. Prediction might be preferred in scenarios like weather forecasting, where accuracy is paramount, while inference is crucial in situations like understanding the impact of marketing strategies on sales, where the reasons behind the predictions are important.",
    'chapter_information': 'ISLR C2, Week 1'
}

islr_c2_q5 = {
    'question': "Explain the distinction between parametric and non-parametric methods. What are the advantages and disadvantages of each?",
    'correct_answer': "Parametric methods involve assuming a specific form for the function that relates the input to the output variables, then estimating the parameters of this function from the data. They are simpler and require less data, but may perform poorly if the chosen form is incorrect. Non-parametric methods do not make explicit assumptions about the form of the function, offering more flexibility to capture complex relationships at the cost of requiring more data and being computationally intensive.",
    'chapter_information': 'ISLR C2, Week 1'
}

islr_c2_q6 = {
    'question': "Discuss the trade-off between prediction accuracy and model interpretability. Why might a more restrictive model sometimes be preferred over a more flexible one?",
    'correct_answer': "There is often a trade-off between prediction accuracy and model interpretability in statistical learning. More complex models may offer higher accuracy but are harder to interpret, while simpler models are easier to understand but may not capture complex patterns as well. A more restrictive model might be preferred in scenarios where understanding the model's decisions is crucial, such as in healthcare or policy-making, even if it sacrifices some degree of prediction accuracy.",
    'chapter_information': 'ISLR C2, Week 1'
}

islr_c2_q2a = {
    'question': "Explain whether the scenario is a classification or regression problem, and indicate whether we are most interested in inference or prediction. Finally, provide n and p. We collect a set of data on the top 500 firms in the US. For each firm we record profit, number of employees, industry and the CEO salary. We are interested in understanding which factors affect CEO salary.",
    'correct_answer': "This is a regression problem because the CEO salary, which is a continuous outcome, serves as the response variable. The interest is in inference, as the goal is to understand the relationship between predictors (profit, number of employees, industry) and the CEO salary. Here, n (the number of observations) is 500, and p (the number of predictors) is 3.",
    'chapter_information': "ISLR C2"
}

islr_c2_q2b = {
    'question': "Explain whether the scenario is a classification or regression problem, and indicate whether we are most interested in inference or prediction. Finally, provide n and p. We are considering launching a new product and wish to know whether it will be a success or a failure. We collect data on 20 similar products that were previously launched. For each product we have recorded whether it was a success or failure, price charged for the product, marketing budget, competition price, and ten other variables.",
    'correct_answer': "This is a classification problem because the outcome (whether the product is a success or a failure) is categorical. The interest is in prediction, aiming to forecast the success or failure of the new product without necessarily understanding the influence of each predictor. In this scenario, n (the number of observations) is 20, and p (the number of predictors) is 13.",
    'chapter_information': "ISLR C2"
}

islr_c2_q2c = {
    'question': "Explain whether the scenario is a classification or regression problem, and indicate whether we are most interested in inference or prediction. Finally, provide n and p. We are interested in predicting the % change in the US Dollar in relation to the weekly changes in the world stock markets. Hence we collect weekly data for all of 2012. For each week we record the % change in the USD/Euro, the % change in the US market, the % change in the British market, and the % change in the German market.",
    'correct_answer': "This is a regression problem because the response variable, % change in the USD/Euro exchange rate, is continuous. The interest is primarily in prediction, as the goal is to forecast the exchange rate change without delving into the specifics of how each market's change influences it. Here, n (the number of observations) is 52, representing weekly data for a year, and p (the number of predictors) is 3.",
    'chapter_information': "ISLR C2"
}

###############################

islr_c3_q1 = {
'question': "Explain how the coefficients in a simple linear regression model are estimated using the least squares method.",
'correct_answer': "In simple linear regression, the coefficients are estimated using the least squares method, which minimizes the sum of the squared residuals—the differences between observed and predicted values. This involves finding the slope and intercept that minimize this sum, resulting in a line that best fits the data.",
'chapter_information': "ISLR C3"
}

islr_c3_q2 = {
'question': "Discuss the assumptions underlying linear regression and how they impact the interpretation of the model coefficients.",
'correct_answer': "Linear regression assumes linearity, independence of errors, constant variance (homoscedasticity) of errors, and normally distributed errors. Violating these assumptions can lead to incorrect inferences about the relationship between predictors and the response, as it affects the reliability of the regression coefficients and the model's predictions.",
'chapter_information': "ISLR C3"
}

islr_c3_q3 = {
'question': "Explain the concept of multiple linear regression and how it differs from simple linear regression.",
'correct_answer': "Multiple linear regression models the relationship between a single dependent variable and multiple independent variables, unlike simple linear regression which involves only one predictor. It allows for the assessment of the impact of each predictor on the response while holding other variables constant.",
'chapter_information': "ISLR C3"
}

islr_c3_q4 = {
'question': "Explain the concept of model fit in linear regression and how R-squared and residual standard error (RSE) are used to assess it.",
'correct_answer': "Model fit in linear regression is assessed by R-squared, indicating the proportion of variance in the response variable explained by the predictors, and Residual Standard Error (RSE), measuring the average deviation of the response from the regression line. High R-squared and low RSE indicate a good fit.",
'chapter_information': "ISLR C3"
}

islr_c3_q5 = {
'question': "Describe how to use F-statistics to test whether at least one predictor is useful in predicting the response in multiple linear regression.",
'correct_answer': "F-statistics test the null hypothesis that all regression coefficients are zero against the alternative that at least one is not. A significant F-test indicates the predictors, as a group, significantly predict the response, suggesting the regression model is useful.",
'chapter_information': "ISLR C3"
}

islr_c3_q6 = {
'question': "Discuss the challenges and strategies for selecting the most important variables in a multiple linear regression model.",
'correct_answer': "Selecting important variables involves avoiding overfitting with too many variables or underfitting with too few. Strategies include forward selection, backward elimination, and stepwise selection, which systematically add or remove predictors based on their statistical significance to the model.",
'chapter_information': "ISLR C3"
}

islr_c3_q7 = {
'question': "How can you detect non-linearity in a linear regression model, and what strategies can you use to address it?",
'correct_answer': "Non-linearity can be detected using residual plots, which show patterns if a linear model is inappropriate. Addressing non-linearity may involve transforming variables (e.g., using log, square root) or adding polynomial terms to the model.",
'chapter_information': "ISLR C3"
}

islr_c3_q8 = {
'question': "Explain how correlation among error terms can affect the results of a linear regression model and how you might detect this issue.",
'correct_answer': "Correlation among error terms violates the independence assumption, leading to underestimated standard errors. This can be detected by examining residuals over time or through Durbin-Watson test, indicating the need for time series models or other adjustments.",
'chapter_information': "ISLR C3"
}

islr_c3_q9 = {
'question': "Describe the problem of non-constant variance of error terms (heteroscedasticity) and how it can be identified and remedied.",
'correct_answer': "Heteroscedasticity, or non-constant variance of error terms, can be identified through funnel-shaped patterns in residual plots. Remedies include transforming the response variable or using weighted least squares to stabilize variance.",
'chapter_information': "ISLR C3"
}

islr_c3_q10 = {
'question': "Discuss the impact of outliers on a linear regression model and how they can be identified and handled.",
'correct_answer': "Outliers can significantly skew regression results. They're identifiable through residual plots or influence measures (e.g., Cook's distance). Handling may involve data transformation, robust regression methods, or exclusion if justified.",
'chapter_information': "ISLR C3"
}

isislr_c3_q11 = {
'question': "Explain what high-leverage points are, how they differ from outliers, and how they can be identified in both simple and multiple linear regression models.",
'correct_answer': "High-leverage points have extreme predictor values that make them distinct from the rest of the data, potentially exerting undue influence on the model's parameters. Unlike outliers, which are extreme in the response variable, high-leverage points are extreme in the predictor(s). They can be identified using leverage statistics; values significantly higher than average suggest high leverage. In multiple regression, plotting leverage scores can help identify these points.",
'chapter_information': "ISLR C3"
}

islr_c3_q12 = {
'question': "Define collinearity and multicollinearity. How do they impact linear regression models, and how can you detect and address them?",
'correct_answer': "Collinearity and multicollinearity refer to situations where two or more predictor variables are closely related to one another. This can inflate the variance of coefficient estimates, making statistical tests less reliable. Detection can be done using the Variance Inflation Factor (VIF) or correlation matrices. Addressing multicollinearity might involve removing or combining correlated variables, or applying regularization techniques like Ridge or Lasso regression.",
'chapter_information': "ISLR C3"
}

islr_c3_q13 = {
'question': "Given an example where two predictors are highly collinear, discuss the potential consequences on the regression analysis and possible solutions to mitigate these effects.",
'correct_answer': "In cases of high collinearity, such as predictors 'limit' and 'rating' being correlated, it becomes difficult to separate their individual effects on the response. This can lead to increased standard errors and unreliable coefficient estimates. Solutions include removing one of the collinear predictors, combining them into a single predictor, or using regularization methods to penalize large coefficients and reduce overfitting.",
'chapter_information': "ISLR C3"
}

islr_c3_q14 = {
'question': "Discuss the use of residual plots in identifying problems with linear regression models. How can they help in detecting non-linearity, heteroscedasticity, and outliers?",
'correct_answer': "Residual plots, which graph the residuals against fitted values or predictors, are crucial for diagnosing regression model issues. Patterns in these plots can indicate non-linearity, suggesting a need for transformation or polynomial terms. Funnel shapes point to heteroscedasticity, potentially requiring transformations or weighted least squares. Large residuals may indicate outliers, necessitating further investigation or remedial measures.",
'chapter_information': "ISLR C3"
}

islr_c3_q15 = {
'question': "Describe the Variance Inflation Factor (VIF) and how it can be used to quantify the degree of multicollinearity among predictors in a regression model.",
'correct_answer': "VIF measures how much the variance of an estimated regression coefficient increases due to multicollinearity. A VIF value greater than 5 or 10 suggests significant multicollinearity. It quantifies the severity of multicollinearity by comparing the variance of the coefficient estimates with and without the other predictors. High VIF values indicate a need to address multicollinearity, potentially by removing variables, combining them, or using regularization techniques.",
'chapter_information': "ISLR C3"
}

#######################lecture notes weeks 1-3

ln_weeks_3_to_5_q1 = {
'question': "Explain the iterative process of regression analysis and identify the key steps involved. How does each step impact the development of a regression model?",
'correct_answer': "The iterative process of regression analysis includes specifying the model, selecting variables, estimating model parameters, assessing model fit and assumptions, and refining the model. Each step is crucial for building a reliable regression model, impacting its accuracy, interpretability, and predictive power.",
'chapter_information': "Lecture Notes Weeks 1-3"
}

ln_weeks_3_to_5_q2 = {
'question': "Discuss the variety of applications for regression analysis in business functions. Can you give examples of how regression analysis can be applied in different sectors such as finance, marketing, and operations?",
'correct_answer': "Regression analysis is widely used in finance to predict stock prices, in marketing to assess the impact of advertising campaigns, and in operations for demand forecasting. Each application helps in decision making by quantifying the relationship between variables.",
'chapter_information': "Lecture Notes Weeks 1-3"
}

ln_weeks_3_to_5_q3 = {
'question': "Discuss the concept of multicollinearity. Why is it a problem in regression analysis, and how can it be detected and addressed?",
'correct_answer': "Multicollinearity occurs when predictors are highly correlated, making it difficult to discern their individual effects on the response. It can lead to unstable coefficient estimates. Detection methods include VIFs, and solutions involve removing or combining correlated variables.",
'chapter_information': "Lecture Notes Weeks 1-3"
}

ln_weeks_3_to_5_q4 = {
'question': "What are the assumptions underlying linear regression? How can the violation of these assumptions affect the results of a regression analysis?",
'correct_answer': "Linear regression assumptions include linearity, independence, homoscedasticity, and normal distribution of residuals. Violations can lead to biased, inefficient, and unreliable estimates, affecting confidence in model predictions and inferences.",
'chapter_information': "Lecture Notes Weeks 1-3"
}

ln_weeks_3_to_5_q5 = {
'question': "Describe the concept of R squared and adjusted R squared. How do they differ, and what does each measure tell you about a regression model?",
'correct_answer': "R squared measures the proportion of variance in the dependent variable explained by the model. Adjusted R squared adjusts for the number of predictors, providing a more accurate measure for models with multiple variables. Both assess model fit but adjusted R squared is more robust for model comparison.",
'chapter_information': "Lecture Notes Weeks 1-3"
}

ln_weeks_3_to_5_q6 = {
'question': "How do outliers and leverage points affect a regression model? What strategies can be employed to identify and mitigate their impact?",
'correct_answer': "Outliers and leverage points can distort the regression model, affecting its accuracy. Identification strategies include residual analysis and leverage plots. Mitigation can involve data transformation, removal of outliers, or employing robust regression techniques.",
'chapter_information': "Lecture Notes Weeks 1-3"
}

ln_weeks_3_to_5_q7 = {
'question': "Explain the purpose of using indicator or dummy variables in regression analysis. How do they enable the modeling of categorical data?",
'correct_answer': "Indicator or dummy variables allow for the inclusion of categorical data in regression models by converting categories into binary variables. This enables the model to distinguish effects of different categories on the response variable.",
'chapter_information': "Lecture Notes Weeks 1-3"
}

ln_weeks_3_to_5_q8 = {
'question': "Discuss the concept of interaction terms in regression models. Why are they important, and how do they alter the interpretation of the model?",
'correct_answer': "Interaction terms model the combined effect of two predictors on the response variable, revealing if the relationship between one predictor and the response changes at different levels of another predictor. They are crucial for understanding complex relationships and can significantly alter model interpretation.",
'chapter_information': "Lecture Notes Weeks 1-3"
}

#######################ISLR C4


islr_c4_q1 = {
'question': "How does logistic regression differ from linear regression, and why is it more suited for classification tasks?",
'correct_answer': "Logistic regression differs from linear regression by predicting the probability that an observation belongs to a particular category, rather than predicting a continuous outcome. It is more suited for classification tasks because it models the odds of belonging to a class via the logistic function, ensuring that the output probabilities range between 0 and 1.",
'chapter_information': "ISLR C4"
}

islr_c4_q2 = {
'question': "Explain the concept of the odds ratio in the context of logistic regression. How can it be interpreted in terms of probability?",
'correct_answer': "In logistic regression, the odds ratio expresses the change in odds resulting from a one-unit change in the predictor variable, holding all other predictors constant. It can be interpreted as the factor by which the odds of the outcome increase (odds ratio > 1) or decrease (odds ratio < 1) with a one-unit increase in the predictor.",
'chapter_information': "ISLR C4"
}

islr_c4_q3 = {
'question': "Discuss the importance of the logistic function in transforming linear regression output to probabilities. How does this transformation facilitate classification?",
'correct_answer': "The logistic function transforms the linear regression output into probabilities by ensuring the output values fall between 0 and 1. This transformation is crucial for classification because it allows the model to express the likelihood of membership in each category, facilitating a clear decision-making process based on probability thresholds.",
'chapter_information': "ISLR C4"
}


islr_c4_q6 = {
'question': "Discuss the assumptions behind logistic regression. How do these assumptions impact the model's performance and interpretation?",
'correct_answer': "Logistic regression assumes linear relationships between the log-odds of the outcome and the predictors, independent observations, and no multicollinearity among predictors. Violating these assumptions can impact model performance by leading to biased or incorrect estimates and making the interpretation of coefficients challenging.",
'chapter_information': "ISLR C4"
}

islr_c4_q9 = {
'question': "Discuss the role of feature selection and regularization in enhancing the performance of a logistic regression model.",
'correct_answer': "Feature selection helps in identifying the most significant predictors, reducing model complexity, and avoiding overfitting. Regularization techniques (L1 and L2) penalize large coefficients, further preventing overfitting and enhancing model performance by keeping the model simple and focused on the most informative features.",
'chapter_information': "ISLR C4"
}
####################################Lectures weeks 3-5

lecture_c45_q13 = {
    'question': "Explain the difference between correlation and causality within the context of business analytics. Why is establishing causality important for making business decisions?",
    'correct_answer': "Correlation indicates a statistical relationship between two variables, whereas causality establishes a cause-and-effect link. Establishing causality is crucial for business decisions because it helps in understanding the impact of one variable on another, guiding strategic actions like pricing adjustments or marketing campaigns to achieve desired outcomes.",
    'chapter_information': "Lecture Notes Weeks 3-5"
}

lecture_c45_q14 = {
    'question': "What is selection bias, and how can it affect the outcomes of business analytics studies?",
    'correct_answer': "Selection bias occurs when the sample is not representative of the population, often due to non-random selection of participants. It can significantly affect study outcomes by leading to incorrect conclusions about relationships or effects, thereby misleading business decisions based on the analytics.",
    'chapter_information': "Lecture Notes Weeks 3-5"
}

lecture_c45_q15 = {
    'question': "Discuss the concept and importance of randomized controlled experiments in establishing causality.",
    'correct_answer': "Randomized controlled experiments randomly assign subjects to treatment and control groups to isolate the effect of the treatment. They are crucial for establishing causality because they minimize selection bias and other confounding factors, providing a clear view of the treatment's impact.",
    'chapter_information': "Lecture Notes Weeks 3-5"
}

lecture_c45_q16 = {
    'question': "Explain the STAR experiment and its significance in educational research.",
    'correct_answer': "The STAR experiment, conducted in Tennessee, studied the effect of class size on student academic achievement by randomly assigning students and teachers to classes of different sizes. Its significance lies in its robust design and clear demonstration of small class sizes improving student performance, influencing educational policies.",
    'chapter_information': "Lecture Notes Weeks 3-5"
}

lecture_c45_q17 = {
    'question': "How do natural experiments differ from randomized controlled experiments, and what is a difference-in-difference estimator?",
    'correct_answer': "Natural experiments arise from external factors or policies, not from random assignment by researchers, making them less controlled but valuable for studying real-world effects. A difference-in-difference estimator compares pre- and post-treatment effects in both treatment and control groups, helping to isolate the treatment's impact.",
    'chapter_information': "Lecture Notes Weeks 3-5"
}

lecture_c45_q18 = {
    'question': "What is selection bias in the context of treatment effects, and how can it be controlled?",
    'correct_answer': "Selection bias in treatment effects occurs when the treatment group is not randomly selected, potentially skewing results. It can be controlled through methods like randomized controlled experiments, natural experiments with appropriate control groups, and adding control variables to the analysis.",
    'chapter_information': "Lecture Notes Weeks 3-5"
}

lecture_c45_q19 = {
    'question': "Discuss the role of counterfactuals in estimating treatment effects and the challenges in establishing them.",
    'correct_answer': "Counterfactuals represent what would have happened without the treatment. They are critical for estimating true treatment effects by providing a comparison baseline. Establishing counterfactuals is challenging due to the difficulty in creating or identifying a control group that accurately represents what the treatment group would have experienced without the intervention.",
    'chapter_information': "Lecture Notes Weeks 3-5"
}

lecture_c45_q20 = {
    'question': "Explain the implications of poorly designed experiments and how they can lead to incorrect conclusions in business analytics.",
    'correct_answer': "Poorly designed experiments, often due to selection bias or confounding variables, can lead to incorrect conclusions by attributing effects to the wrong causes. This misguidance can result in ineffective or detrimental business strategies, emphasizing the importance of careful experimental design.",
    'chapter_information': "Lecture Notes Weeks 3-5"
}

lecture_c45_q21 = {
    'question': "What are the considerations for using control variables in regression models to estimate treatment effects?",
    'correct_answer': "Control variables are used in regression models to account for potential confounding factors, isolating the treatment's effect. Considerations include selecting relevant variables that influence the outcome but are not affected by the treatment, ensuring they do not introduce multicollinearity, and understanding their limitations in fully accounting for all confounding effects.",
    'chapter_information': "Lecture Notes Weeks 3-5"
}

#################################### Week 5

lecture_notes_week5_q1 = {
    'question': "What is program evaluation, and how does the difference-in-difference (DiD) estimator apply to it?",
    'correct_answer': "Program evaluation aims to assess the impact of a program or treatment on an outcome over a population. The DiD estimator is used to compare the changes in outcomes over time between a treatment group and a control group, helping to isolate the effect of the intervention by accounting for trends that affect both groups.",
    'chapter_information': "Lecture and Reading Week 5"
}

lecture_notes_week5_q2 = {
    'question': "Discuss the assumptions necessary for the difference-in-difference estimator to provide an unbiased estimate.",
    'correct_answer': "For the DiD estimator to be unbiased, several assumptions must hold: the model is correctly specified, the error term averages to zero and is uncorrelated with the predictors, and importantly, the parallel trend assumption, meaning that in the absence of treatment, the difference between the treatment and control groups would remain constant over time.",
    'chapter_information': "Lecture and Reading Week 5"
}

lecture_notes_week5_q3 = {
    'question': "Explain how the parallel trend assumption underpins the validity of the difference-in-difference estimator.",
    'correct_answer': "The parallel trend assumption posits that, in the absence of treatment, the trends in outcomes for both treatment and control groups would have moved in parallel over time. This assumption is crucial because it allows the DiD estimator to attribute differences in outcome changes to the treatment, rather than to pre-existing trends.",
    'chapter_information': "Lecture and Reading Week 5"
}

lecture_notes_week5_q4 = {
    'question': "How can violations of the parallel trend assumption affect the estimates provided by the DiD method?",
    'correct_answer': "Violations of the parallel trend assumption can lead to biased estimates, as the DiD method may incorrectly attribute changes in the outcome to the treatment that are actually due to divergent trends between the treatment and control groups prior to the intervention.",
    'chapter_information': "Lecture and Reading Week 5"
}

lecture_notes_week5_q5 = {
    'question': "Describe strategies for addressing violations of the parallel trend assumption in DiD analysis.",
    'correct_answer': "To address violations of the parallel trend assumption, researchers can extend the DiD framework to include additional time periods or control groups, allowing for the examination of pre-existing trends. Additionally, using robustness checks or incorporating covariates that capture potential confounders can help mitigate the impact of these violations.",
    'chapter_information': "Lecture and Reading Week 5"
}

lecture_notes_week5_q6 = {
    'question': "What role does the error term play in the DiD model, and how are its properties critical to the model's assumptions?",
    'correct_answer': "The error term in the DiD model captures all unobserved factors affecting the outcome. For the model's assumptions to hold, this error term must have a mean of zero and be uncorrelated with other variables in the model. These properties ensure unbiased and consistent estimates of the treatment effect.",
    'chapter_information': "Lecture and Reading Week 5"
}

lecture_notes_week5_q7 = {
    'question': "Discuss the importance of choosing appropriate control groups in the application of the DiD estimator.",
    'correct_answer': "Choosing appropriate control groups is vital for DiD analysis because they provide a benchmark for estimating what would have happened to the treatment group in the absence of the intervention. The validity of DiD estimates heavily relies on the control group's comparability to the treatment group, ensuring that the parallel trend assumption is plausible.",
    'chapter_information': "Lecture and Reading Week 5"
}

lecture_notes_week5_q8 = {
    'question': "Explain how the DiD estimator is derived from comparing pre-treatment and post-treatment differences between the treatment and control groups.",
    'correct_answer': "The DiD estimator is derived by calculating the difference in average outcomes before and after the treatment for both groups and then taking the difference of these differences. This approach effectively controls for fixed differences between the groups and common trends affecting both groups, isolating the treatment effect.",
    'chapter_information': "Lecture and Reading Week 5"
}

lecture_notes_week5_q9 = {
    'question': "How can external factors or events potentially bias DiD estimates, and what mitigation strategies can be employed?",
    'correct_answer': "External factors or events that differentially affect the treatment and control groups can bias DiD estimates by violating the parallel trend assumption. Mitigation strategies include incorporating covariates to adjust for these factors, conducting sensitivity analyses, and selecting control groups not exposed to the external influences.",
    'chapter_information': "Lecture and Reading Week 5"
}

lecture_notes_week5_q10 = {
    'question': "Illustrate with an example how the DiD approach has been applied in empirical research to estimate the effect of policy interventions.",
    'correct_answer': "An example of DiD application is the study by Card and Krueger (1994) on the effect of minimum wage increase on employment in the fast-food industry in New Jersey compared to Pennsylvania. They used employment data from before and after the wage increase as treatment and control groups, respectively, to isolate the impact of the minimum wage rise. This study highlighted the effectiveness of DiD in assessing policy impacts when parallel trend assumptions hold.",
    'chapter_information': "Lecture Notes Weeks 3-5"
}






OPEN_QUESTIONS = []
global_items = list(globals().items())

for name, value in global_items:
    if not name.startswith('_'):
        OPEN_QUESTIONS.append(value)

OPEN_QUESTIONS = OPEN_QUESTIONS[:-1]
