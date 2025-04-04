import Orange
from Orange.data import Table

# Load your stock data (assuming CSV format)
data = Table("path_to_your_stock_data.csv")

# Basic data exploration
print(f"Number of instances: {len(data)}")
print(f"Number of variables: {len(data.domain.attributes)}")
print(f"Feature names: {[attr.name for attr in data.domain.attributes]}")

# First few rows
print(data[:5])