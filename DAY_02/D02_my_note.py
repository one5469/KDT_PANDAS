import pandas as pd

filename = '../DATA/deliveries.csv'
data = pd.read_csv(filename)
print(data)

print(data.loc[0])
print(data.keys())
print(data.index)
print(data.columns)
ser = data['order_date']

print(ser.name)
print(ser.dtype)
print(ser.keys())
print(ser.index)