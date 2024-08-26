import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def selection_sort(arr, update_func):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        update_func(arr)
        yield arr


def update_plot(arr):
    for bar, height in zip(bars, arr):
        bar.set_height(height)
    plt.draw()
    plt.pause(0.1)


arr = np.random.randint(1, 100, size=20)
fig, ax = plt.subplots()
bars = ax.bar(range(len(arr)), arr, color='blue')
ax.set_title('Selection Sort Visualization')
ax.set_xlabel('Index')
ax.set_ylabel('Value')
plt.ylim(0, max(arr) + 10)


def animate(frame):
    update_plot(frame)


ani = FuncAnimation(fig, animate, frames=selection_sort(list(arr), update_plot), repeat=False, interval=100)
plt.show()
