python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pip install orange3
pip install orange3-timeseries
pip install orange3-associate
python -m Orange.canvas

import Orange
from Orange.data import Table

# Load your stock data (assuming CSV format)
data = Table("path_to_your_stock_data.csv")
python -m Orange.canvas