import numpy as np
from sklearn.ensemble import RandomForestClassifier
from hummingbird.ml import convert

# Generate dummy data
X = np.random.rand(10000, 28)
y = np.random.randint(2, size=10000)

# Train a traditional model
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# Convert to a PyTorch model (can use 'cuda' for GPU)
hb_model = convert(model, 'torch', device='cuda')

# Run inference on GPU
X_test = np.random.rand(1000, 28)
predictions = hb_model.predict(X_test)