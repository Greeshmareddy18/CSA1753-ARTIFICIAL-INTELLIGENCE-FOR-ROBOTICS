import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# XOR input
X = np.array([[0,0],
              [0,1],
              [1,0],
              [1,1]])

# Fixed weights and bias
wh = np.array([[20, -20],
               [20, -20]])
bh = np.array([[-10, 30]])

wo = np.array([[20],
               [20]])
bo = np.array([[-30]])

# Feed forward
hidden = sigmoid(np.dot(X, wh) + bh)
output = sigmoid(np.dot(hidden, wo) + bo)

# Binary output
result = (output >= 0.5).astype(int)

print("Output:")
print("".join(map(str, result.flatten())))
