# Import standard library for time measurement
import time
# Import PyTorch for building and training neural networks
import torch
# Import the neural network module from PyTorch
import torch.nn as nn

# Set a fixed random seed for reproducibility
torch.manual_seed(0)

# Define a simple Multi-Layer Perceptron (MLP) neural network
class SimpleMLP(nn.Module):
    def __init__(self, input_size=128, hidden_size=516, output_size=1):
        """
        Initialize the MLP with fully connected layers and ReLU activations.

        Args:
            input_size (int): Number of input features (default: 128)
            hidden_size (int): Number of neurons in hidden layers (default: 516)
            output_size (int): Number of output neurons (default: 1)
        """
        super().__init__()
        # First fully connected layer: input -> hidden
        self.fc1 = nn.Linear(input_size, hidden_size)
        # ReLU activation after the first layer
        self.relu1 = nn.ReLU()
        # Second fully connected layer: hidden -> hidden
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        # ReLU activation after the second layer
        self.relu2 = nn.ReLU()
        # Third fully connected layer: hidden -> output
        self.fc3 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        """
        Define the forward pass of the network.

        Args:
            x (Tensor): Input tensor of shape (batch_size, input_size)

        Returns:
            Tensor: Output tensor of shape (batch_size, output_size)
        """
        # Apply first linear layer then ReLU activation
        x = self.relu1(self.fc1(x))
        # Apply second linear layer then ReLU activation
        x = self.relu2(self.fc2(x))
        # Apply output layer (no activation for regression output)
        x = self.fc3(x)
        return x

# Instantiate the model with default parameters
model = SimpleMLP()

# Import custom summary utility to display model architecture
from custom_torchinfo import custom_summary
# Print a summary of the model with a sample input size (batch=64, features=128)
custom_summary(model, input_size=(64, 128))
