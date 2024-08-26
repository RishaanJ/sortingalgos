import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import random


def bogo_sort(arr, update_func):
    def is_sorted(arr):
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

    while not is_sorted(arr):
        random.shuffle(arr)
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

ax.set_title('Bogo Sort Visualization')
ax.set_xlabel('Index')
ax.set_ylabel('Value')
plt.ylim(0, max(arr) + 10)


def animate(frame):
    update_plot(frame)


ani = FuncAnimation(fig, animate, frames=bogo_sort(arr, update_plot), repeat=False, interval=100)

plt.show()
