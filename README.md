# This code helps in finding top n accuracy for a classification problem.

 - Eg: let's say you have 100 classes for your target variable
 - For a given classification model, if you're fine even if the required result is in the top three results instead of just the result predicted by the model
 - Implies, if a1,a2,a3...a100 are the classes you have for the target variable
 - If the required result is the third best according to the model probability and still if you want to flag that as successful prediction,
 - You may simply provide the model with
   - model = any classification model from scikit-learn
   - X_test = independent variables
   - y_test = The correct labels for the record
   - n_value = 3/4/5 etc any number less than number of categories in class variable 
