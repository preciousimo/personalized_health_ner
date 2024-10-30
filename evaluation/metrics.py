from sklearn.metrics import classification_report

def evaluate(y_true, y_pred):
    return classification_report(y_true, y_pred)
