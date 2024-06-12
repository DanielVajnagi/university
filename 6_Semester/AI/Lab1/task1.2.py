import numpy as np
data = np.array([0.1, 5.9, 0.5, 4.0, 0.3, 5.5, 0.1, 4.5, 0.6, 4.3, 1.5, 4.7, 0.5, 5.8, 0.0])

scale = np.max(data)

class Neural:
    def __init__(self):
        self.weights = np.random.rand(2)
    def sigmoid(self, x):
        return 1/(1+ np.exp(-x))
    def predict(self, inputs):
        weighted_sum = np.dot(inputs, self.weights)
        return self.sigmoid(weighted_sum)
    def train(self, inputs, expected_output, epochs):
        learning_rate = 0.1
        for _ in range(epochs):
            for i in range(len(inputs)):
                prediction = self.predict(inputs[i])
                error = expected_output[i] - prediction
                self.weights += learning_rate * error * prediction * (1 - prediction) * inputs[i]

X_time_series = np.array([ [0.1, 5.9], [5.9, 0.5], [0.5, 4.0], [4.0, 0.3], [0.3, 5.5],
    [5.5, 0.1], [0.1, 4.5], [4.5, 0.6], [0.6, 4.3], [4.3, 1.5], [1.5, 4.7]])/scale
y_time_series = np.array([0.5, 4.0, 0.3, 5.5, 0.1, 4.5, 0.6, 4.3, 1.5, 4.7, 0.5])/scale

neural = Neural()
neural.train(X_time_series, y_time_series, epochs=1000)

#Prediction for the new input values
predicted_values = [neural.predict([4.7,0.5])*scale] 
predicted_values = [neural.predict([0.5,5.8])*scale] 

print("Predicted value for x_14:", neural.predict([4.7,0.5])*scale,"Expected value=5.8")
print("Predicted value for x_15:", neural.predict([0.5,5.8])*scale,"Expected value=0")