import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def insertion_sort(arr, update_func):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
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
ax.set_title('Insertion Sort Visualization')
ax.set_xlabel('Index')
ax.set_ylabel('Value')
plt.ylim(0, max(arr) + 10)


def animate(frame):
    update_plot(frame)


ani = FuncAnimation(fig, animate, frames=insertion_sort(list(arr), update_plot), repeat=False, interval=100)
plt.show()
