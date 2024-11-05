import joblib

def load_model():
    # Load the model once to save resources
    return joblib.load('random_forest_model.pkl')

def predict_obesity(model, input_data):
    # Generate the prediction
    return model.predict(input_data)[0]
