import matplotlib.pyplot as plt

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
temperatures = [22, 24, 19, 23, 25, 27, 55]
plt.plot(days, temperatures, marker='o')

plt.title('Temperature Variation Over a Week')
plt.xlabel('Day of the Week')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()