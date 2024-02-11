import pandas

data=pandas.read_csv('weather_data.csv')
print(f"{data['temp'].mean():.2f}")
print(data['temp'].max())
print(data[data.day == 'Monday'])
print(data[data.temp == data.temp.max()])