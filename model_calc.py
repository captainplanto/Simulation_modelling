import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate random data
time = np.arange(0, 10, 0.1)
value = np.random.rand(len(time))
parameter = np.random.randint(1, 10, len(time))

# Create DataFrame
data = pd.DataFrame(
    {
        "time": time,
        "value": value,
        "parameter": parameter,
    }
)
data.to_csv("models.csv", index=False)
