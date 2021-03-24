import matplotlib.pyplot as plt

x_coords = [0, 1, 2, 3, 4]
y_coords = [4, 3, 2, 1, 0]

plt.plot(x_coords, y_coords)
plt.title("some title")
plt.xlabel("x axis")
plt.ylabel("y axis")

plt.grid(True)

plt.show()
