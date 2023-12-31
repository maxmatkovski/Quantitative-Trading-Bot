# CREATE BASIC NEURAL NETWORK FROM SCRATCH TO UNDERSTAND THE MECHANISM
import numpy as np 

# INITIALIZE SIGMOID AND SIZES
def sigmoid(x):
    return (1 / (1+np.exp(-x)))

def sigmoid_derivative(x):
    return x * (1-x)

input_size = 3  # Number of input neurons (features)
hidden_size = 4  # Number of hidden neurons
output_size = 1  # Number of output neurons

# WEIGHTS AND BIASES INITIALIZATION
weights_input_hidden = np.random.randn(input_size, hidden_size)
weights_hidden_output = np.random.randn(hidden_size, output_size)
bias_hidden = np.zeros((1, hidden_size))
bias_output = np.zeros((1, output_size))

# FORWARD PASS FUNCTION
def forward_pass(input_data):
    hidden_layer_input = np.dot(input_data, weights_input_hidden) + bias_hidden
    hidden_layer_output = sigmoid(hidden_layer_input)

    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
    predicted_output = sigmoid(output_layer_input)
    
    return predicted_output, hidden_layer_output

# BACKPROPOGATION FUNCTION
def backpropagation(input_data, actual_output, predicted_output, hidden_layer_output):
    global weights_input_hidden, bias_hidden, weights_hidden_output, bias_output

    error = actual_output - predicted_output
    d_predicted_output = error * sigmoid_derivative(predicted_output)

    error_hidden_layer = d_predicted_output.dot(weights_hidden_output.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

    # Updating Weights and Biases
    weights_hidden_output += hidden_layer_output.T.dot(d_predicted_output)
    bias_output += np.sum(d_predicted_output, axis=0, keepdims=True)

    weights_input_hidden += input_data.T.dot(d_hidden_layer)
    bias_hidden += np.sum(d_hidden_layer, axis=0, keepdims=True)


# TRAINING WITH SOME SAMPLE DATA
# Example data (X) and labels (Y)
X = np.array([[0, 0, 1],
              [1, 1, 1],
              [1, 0, 1],
              [0, 1, 1]])
Y = np.array([[0], [1], [1], [0]])

# Training loop
for epoch in range(10000):
    predicted_output, hidden_layer_output = forward_pass(X)
    backpropagation(X, Y, predicted_output, hidden_layer_output)

# Print final predicted output
print(predicted_output)
