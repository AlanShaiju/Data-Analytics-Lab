import numpy as np

# Sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Initialize the neural network parameters
input_size = 3
hidden_size = 4
output_size = 1
learning_rate = 0.9
epochs = 100000

# Initialize weights and biases with random values
np.random.seed(42)
weights_input_hidden = np.random.uniform(size=(input_size, hidden_size))
weights_hidden_output = np.random.uniform(size=(hidden_size, output_size))
biases_hidden = np.zeros((1, hidden_size))
biases_output = np.zeros((1, output_size))

# Training data
X = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
y = np.array([[0], [1], [1], [0]])

# Training the neural network using backpropagation
for epoch in range(epochs):
    # Forward pass
    hidden_layer_output = sigmoid(np.dot(X, weights_input_hidden) + biases_hidden)
    predicted_output = sigmoid(np.dot(hidden_layer_output, weights_hidden_output) + biases_output)

    # Calculate error
    error = y - predicted_output

    # Backward pass
    output_error = error * sigmoid_derivative(predicted_output)
    hidden_layer_error = output_error.dot(weights_hidden_output.T) * sigmoid_derivative(hidden_layer_output)

    # Update weights and biases
    weights_hidden_output += hidden_layer_output.T.dot(output_error) * learning_rate
    weights_input_hidden += X.T.dot(hidden_layer_error) * learning_rate
    biases_output += np.sum(output_error, axis=0, keepdims=True) * learning_rate
    biases_hidden += np.sum(hidden_layer_error, axis=0, keepdims=True) * learning_rate

# Print the final predicted output
print("Predicted Output after Training:")
print(predicted_output)
