import torch
import torch.nn as nn

# Model
class LinearRegressionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)

# Create model and dummy input
model = LinearRegressionModel()
x = torch.tensor([[5.0]])  # Example input

# Predict
model.eval()
with torch.no_grad():
    prediction = model(x)
    print("Prediction:", prediction.item())
