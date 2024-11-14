import pandas as pd
from sklearn.linear_model import LinearRegression

# Load sales data
data = pd.DataFrame({
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'sales': [50000, 55000, 45000, 60000, 52000, 58000, 62000, 48000, 55000, 57000, 54000, 60000]
})

# Encode month as numeric feature
data['month_num'] = data['month'].apply(lambda x: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'].index(x) + 1)

# Split into features and target
X = data['month_num'].values.reshape(-1, 1)
y = data['sales'].values

# Train linear regression model
model = LinearRegression()
model.fit(X, y)

# Make predictions
forecast = model.predict([[13]]) # Forecast for next month (Jan)
print(f"Forecasted sales for next month: {int(forecast[0])}")