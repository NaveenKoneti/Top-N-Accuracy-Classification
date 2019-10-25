import pandas as pd



def topNAccuracy(model,X_test,y_test,n_value):
    probabilities = model.predict_proba(X_test)
    all_top_n = []
    X_test = pd.DataFrame(X_test)
    X_test['OriginalValue'] = y_test
    prediction_columns = ["Prediction_%s" % num for num in range(n_value)]
    
    for i in range(len(X_test)):
        prediction_top_n = sorted( zip( model.classes_, probabilities[i] ), key=lambda x:x[1] )[-n_value:]
        all_top_n = all_top_n + [prediction_top_n]

    for index, column in enumerate(prediction_columns):
        X_test[column] = [l[n_value - 1 - index][0] for l in all_top_n]
    X_test_predictions = X_test[['OriginalValue']+prediction_columns] 
    X_test_predictions["exists"] = X_test_predictions.drop("OriginalValue", 1).isin(X_test_predictions["OriginalValue"]).any(1)
    accuracy = (len(X_test_predictions[X_test_predictions["exists"] == True])/len(X_test_predictions))*100
    accuracy = round(accuracy,2)
    return accuracy
