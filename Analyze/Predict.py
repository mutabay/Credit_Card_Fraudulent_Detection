
import pickle
import numpy as np

class ModelOperations():
    def __init__(self, transactions):
        self.transactions = transactions
        self.transactions_float = [float(transaction) for transaction in transactions]
        self.result = None

    def predict(self):
        loaded_model = self.load_configured_model()
        vect = np.array(self.transactions_float).reshape(1, -1)
        my_prediction = loaded_model.predict(vect)  # Predict returns 1-1 dimension matrix (just result)

        self.result = int(my_prediction[0])

        return self.result

    def load_configured_model(self):
        # load the model from disk
        filename = 'Analyze/Models/model.pkl'
        loaded_model = pickle.load(open(filename, 'rb'))
        print("Loaded model from disk")

        return loaded_model
