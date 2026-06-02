import time
import torch
import torch.nn as nn
torch.manual_seed(0)

class SimpleMLP(nn.Module):
    def __init__(self, input_size=128, hidden_size=516, output_size=1):
        super().__init__()
        self.fc1   = nn.Linear(input_size, hidden_size)
        self.relu1 = nn.ReLU()
        self.fc2   = nn.Linear(hidden_size, hidden_size)
        self.relu2 = nn.ReLU()
        self.fc3   = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.relu1(self.fc1(x))
        x = self.relu2(self.fc2(x))
        x = self.fc3(x)
        return x

model = SimpleMLP()

from custom_torchinfo import custom_summary
custom_summary(model, input_size=(64, 128))
