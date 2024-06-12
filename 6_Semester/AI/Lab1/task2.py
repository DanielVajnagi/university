class Custom_Neuron:
    def __init__(self):
        self.weights = [0, 0, 0]  # Ваги для x1, x2, x3
        self.bias = 0
        self.learning_rate = 0.1

    def activate(self, weighted_sum):
        return 1 if weighted_sum >= 0 else 0

    def predict(self, inputs):
        weighted_sum = sum(w * x for w, x in zip(self.weights, inputs)) + self.bias
        return self.activate(weighted_sum)

    def train(self, training_inputs, labels, epochs):
        for _ in range(epochs):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                if prediction != label:
                    error = label - prediction
                    for i in range(len(self.weights)):
                        self.weights[i] += error * inputs[i] * self.learning_rate
                    self.bias += error * self.learning_rate


# Таблиця істинності для навчання
training_inputs = [(0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 1)]
labels = [1, 1, 0, 1]

neuron = Custom_Neuron()
neuron.train(training_inputs, labels, epochs=1000)

print("x1 x2 x3 y")
for inputs, label in zip(training_inputs, labels):
    result = neuron.predict(inputs)
    print(f"{inputs[0]}  {inputs[1]}  {inputs[2]}  {result}")
